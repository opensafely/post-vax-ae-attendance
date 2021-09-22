
# # # # # # # # # # # # # # # # # # # # #
# This script:
# creates metadata for aspects of the study design
# # # # # # # # # # # # # # # # # # # # #

# Import libraries ----
library('tidyverse')
library('here')
library('glue')

# create output directories ----
fs::dir_create(here("analysis", "lib"))

# create key dates ----

dates <-
  list(
    start_date = "2020-12-08",
    start_date_pfizer = "2020-12-08",
    start_date_az = "2021-01-04",
    start_date_moderna = "2021-04-07",
    end_date = "2021-08-01"
  )

jsonlite::write_json(dates, path = here("analysis", "lib", "dates.json"), auto_unbox = TRUE, pretty=TRUE)


# parse diagnosis codes ----

# choose which grouping to use here
GroupCustom <- 2

# import codes and group look-up
diagnosis_list <- readxl::read_xlsx(here("analysis", "lib", "diagnosis_codes.xlsx"), sheet="diagnoses")
diagnosis_lookup <- readxl::read_xlsx(here("analysis", "lib", "diagnosis_codes.xlsx"), sheet="groupings") %>%
  filter(grouping==GroupCustom) %>%
  select(-grouping)

# one row per group
diagnosis_groups <-
  diagnosis_list %>%
  rename(group = glue("ECDS_GroupCustom{GroupCustom}")) %>%
  group_by(group) %>%
  summarise(
    codelist = list(SNOMED_Code)
  ) %>%
  left_join(diagnosis_lookup, by="group") %>%
  ungroup()

## check groupings ----

check_groups_a <- unique(diagnosis_list[[glue("ECDS_GroupCustom{GroupCustom}")]])
check_groups_b <-diagnosis_lookup %>%
  pull(group) %>%
  unique()
stopifnot("some diagnosis groups in sheet are not present in look-up" = all(check_groups_a %in% check_groups_b))
stopifnot("some diagnosis groups in look-up are not present in sheet" = all(check_groups_b %in% check_groups_a))


## output formatted codes ----
diagnosis_groups %>%
  select(group, codelist) %>%
  {set_names(.$codelist, .$group)} %>% # convert tibble to list in a slightly awkward way
  jsonlite::write_json(
    path = here("analysis", "lib", "diagnosis_codes.json"),
    #    flatten = TRUE
  )

diagnosis_groups %>%
  select(group, description, codelist) %>%
  write_rds(path = here("analysis", "lib", "diagnosis_codes_lookup.rds"))



# variable labels ----


## variable labels
variable_labels <-
  list(
    vax1_type ~ "Vaccine type",
    vax1_type_descr ~ "Vaccine type",
    age ~ "Age",
    ageband ~ "Age",
    sex ~ "Sex",
    ethnicity_combined ~ "Ethnicity",
    imd_Q5 ~ "IMD",
    region ~ "Region",
    stp ~ "STP",
    vax1_day ~ "Day of vaccination",
    jcvi_group ~ "JCVI priority group"
  ) %>%
  set_names(., map_chr(., all.vars))

write_rds(variable_labels, here("analysis", "lib", "variable_labels.rds"))

