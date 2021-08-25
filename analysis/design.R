
# # # # # # # # # # # # # # # # # # # # #
# This script:
# creates metadata for aspects of the study design
# # # # # # # # # # # # # # # # # # # # #

# Import libraries ----
library('tidyverse')
library('here')

# create output directories ----
fs::dir_create(here("analysis", "lib"))

# create key dates ----

dates <-
  list(
    start_date = "2020-12-08",
    start_date_pfizer = "2020-12-08",
    start_date_az = "2021-01-04",
    start_date_moderna = "2021-03-04",
    end_date = "2021-06-01"
  )

jsonlite::write_json(dates, path = here("analysis", "lib", "dates.json"), auto_unbox = TRUE, pretty=TRUE)


# parse diagnosis codes ----

diagnosis_codes <- readxl::read_xlsx(here("analysis", "lib", "diagnosis_groups.xlsx"))

diagnosis_groups <-
  diagnosis_codes %>%
  rename(group = ECDS_GroupCustomShort) %>%
  mutate(
    group = if_else(is.na(group), "na", group)
  ) %>%
  group_by(ECDS_GroupCustom, group) %>%
  summarise(
    codelist = list(SNOMED_Code)
  ) %>%
  ungroup()


#table(diagnosis_groups$ECDS_GroupCustom, diagnosis_groups$group, useNA='ifany')
#table(diagnosis_groups$group, diagnosis_groups$ECDS_GroupCustom,  useNA='ifany')

diagnosis_groups %>%
  select(group, codelist) %>%
  {set_names(.$codelist, .$group)} %>% # convert tibble to list in a slightly awkward way
  jsonlite::write_json(
    path = here("analysis", "lib", "diagnosis_groups.json"),
    #    flatten = TRUE
  )

diagnosis_groups %>%
  select(group, ECDS_GroupCustom, codelist) %>%
  write_rds(path = here("analysis", "lib", "diagnosis_groups_lookup.rds"))



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

