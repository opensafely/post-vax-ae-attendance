
# # # # # # # # # # # # # # # # # # # # #
# This script creates a "table1" table of patient characteristics by vaccine type
# no automatic redaction!
# # # # # # # # # # # # # # # # # # # # #


## Import libraries ----
library('tidyverse')
library('here')
library('glue')
library('gt')
library('gtsummary')

## Import custom user functions from lib

source(here("analysis", "lib", "utility_functions.R"))

## create output directories ----
fs::dir_create(here("output", "table1"))


## import labels ----
variable_labels <- read_rds(here("analysis", "lib", "variable_labels.rds"))

## Import processed data ----
data_cohort <- read_rds(here("output", "data", "data_cohort.rds"))


## baseline variables
tab_summary_baseline <- data_cohort %>%
  select(
    all_of(names(variable_labels)),
    -age, -stp, -vax1_type
  ) %>%
  tbl_summary(
    by = vax1_type_descr,
    label=unname(variable_labels[names(.)])
  )  %>%
  modify_footnote(starts_with("stat_") ~ NA)

tab_summary_baseline$inputs$data <- NULL

tab_csv <- tab_summary_baseline$table_body
names(tab_csv) <- tab_summary_baseline$table_header$label
tab_csv <- tab_csv[, (!tab_summary_baseline$table_header$hide | tab_summary_baseline$table_header$label=="variable")]

write_rds(tab_summary_baseline, here("output", "table1", "table1.rds"))
gtsave(as_gt(tab_summary_baseline), here("output", "table1", "table1.html"))
write_csv(tab_csv, here("output", "table1", "table1.csv"))

tab_summary_region <- data_cohort %>%
  select(
    region, stp, vax1_type_descr
  ) %>%
  tbl_summary(
    by = vax1_type_descr,
    label=unname(variable_labels[names(.)])
  )  %>%
  modify_footnote(starts_with("stat_") ~ NA)

tab_summary_region$inputs$data <- NULL

tab_region_csv <- tab_summary_region$table_body
names(tab_region_csv) <- tab_summary_region$table_header$label
tab_region_csv <- tab_region_csv[, (!tab_summary_region$table_header$hide | tab_summary_region$table_header$label=="variable")]

gtsave(as_gt(tab_summary_region), here("output", "table1", "table1_regions.html"))
write_csv(tab_csv, here("output", "table1", "table1_regions.csv"))

