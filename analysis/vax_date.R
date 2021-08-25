# # # # # # # # # # # # # # # # # # # # #
# This script plots the cumulative number of people who are vaccinated, by vaccine type
# # # # # # # # # # # # # # # # # # # # #


## Import libraries ----
library('tidyverse')
library('here')
library('glue')
library('survival')

## Import custom user functions from lib
source(here::here("analysis", "lib", "utility_functions.R"))
source(here::here("analysis", "lib", "redaction_functions.R"))
source(here::here("analysis", "lib", "survival_functions.R"))


args <- commandArgs(trailingOnly=TRUE)
if(length(args)==0){
  # use for interactive testing
  removeobs <- FALSE
} else {
  removeobs <- TRUE
}

## import global vars ----
studydates <- jsonlite::read_json(
  path=here("analysis","lib", "dates.json")
)

## import labels ----
variable_labels <- read_rds(here("analysis", "lib", "variable_labels.rds"))

## create output directory ----
fs::dir_create(here("output", "vaxdate"))

data_cohort <- read_rds(here::here("output", "data", "data_cohort.rds"))

cumulvax <- data_cohort %>%
  group_by(vax1_type_descr, vax1_date) %>%
  summarise(
    n=n()
  ) %>%
  ungroup() %>%
  complete(
    vax1_type_descr,
    vax1_date=full_seq(vax1_date,1),
    fill = list(n = 0)
  ) %>%
  add_row(
    vax1_type_descr = unique(.$vax1_type_descr),
    vax1_date = min(.$vax1_date) - 1,
    n=0,
    .before=1
  ) %>%
  group_by(vax1_type_descr) %>%
  mutate(
    cumuln = cumsum(n)
  ) %>%
  arrange(vax1_type_descr, vax1_date) %>%
  ungroup()


plot_stack <-
  ggplot(cumulvax)+
  geom_area(
    aes(
      x=vax1_date+1, y=cumuln,
      group=vax1_type_descr,
      fill=vax1_type_descr
    ),
    alpha=0.5
  )+
  scale_x_date(
    breaks = seq(floor_date(min(cumulvax$vax1_date), "month"), max(cumulvax$vax1_date)+1,by=14),
    limits = c(lubridate::floor_date(min(cumulvax$vax1_date), "1 month"), NA),
    labels = scales::date_format("%d/%m"),
    expand = expansion(0),
    sec.axis = sec_axis(
      trans = ~as.Date(.),
      breaks=as.Date(seq(floor_date(min(cumulvax$vax1_date), "month"), ceiling_date(max(cumulvax$vax1_date), "month"),by="month")),
      labels = scales::date_format("%b %y")
    )
  )+
  scale_fill_brewer(type="qual", palette="Set2")+
  labs(
    x="Date",
    y="Vaccinated, n",
    colour=NULL,
    fill=NULL,
    alpha=NULL
  ) +
  theme_minimal()+
  theme(
    axis.text.x.top=element_text(hjust=0),
    axis.ticks.x.top=element_line(),
    legend.position = "bottom"
  )


plot_step <-
  ggplot(cumulvax)+
  geom_step(
    aes(
      x=vax1_date+1, y=cumuln,
      group=vax1_type_descr,
      colour=vax1_type_descr
    )
  )+
  scale_x_date(
    breaks = seq(floor_date(min(cumulvax$vax1_date), "month"), max(cumulvax$vax1_date)+1,by=14),
    limits = c(lubridate::floor_date((min(cumulvax$vax1_date)), "1 month"), NA),
    labels = scales::date_format("%d/%m"),
    expand = expansion(0),
    sec.axis = sec_axis(
      trans = ~as.Date(.),
      breaks=as.Date(seq(floor_date(min(cumulvax$vax1_date), "month"), ceiling_date(max(cumulvax$vax1_date), "month"),by="month")),
      labels = scales::date_format("%b %y")
    )
  )+
  scale_colour_brewer(type="qual", palette="Set2")+
  labs(
    x="Date",
    y="Vaccinated, n",
    colour=NULL,
    fill=NULL,
    alpha=NULL
  ) +
  theme_minimal()+
  theme(
    axis.text.x.top=element_text(hjust=0),
    axis.ticks.x.top=element_line(),
    legend.position = "bottom"
  )


write_rds(plot_step, here("output", "vaxdate", "plot_vaxdate_step.rds"))
write_rds(plot_stack, here("output", "vaxdate", "plot_vaxdate_stack.rds"))

ggsave(plot_step, filename="plot_vaxdate_step.png", path=here("output", "vaxdate"))
ggsave(plot_stack, filename="plot_vaxdate_stack.png", path=here("output", "vaxdate"))






## by JVCI group

cumulvax <- data_cohort %>%
  group_by(vax1_type_descr, jcvi_group, vax1_date) %>%
  summarise(
    n=n()
  ) %>%
  ungroup() %>%
  complete(
    vax1_type_descr,
    jcvi_group,
    vax1_date=full_seq(c(min(vax1_date-1),vax1_date),1),
    fill = list(n = 0)
  ) %>%
  group_by(vax1_type_descr, jcvi_group) %>%
  mutate(
    cumuln = cumsum(n)
  ) %>%
  arrange(vax1_type_descr, jcvi_group, vax1_date) %>%
  ungroup()


plot_stack <-
  ggplot(cumulvax)+
  geom_area(
    aes(
      x=vax1_date+1, y=cumuln,
      group=vax1_type_descr,
      fill=vax1_type_descr
    ),
    alpha=0.5
  )+
  facet_grid(rows=vars(jcvi_group))+
  scale_x_date(
    breaks = seq(floor_date(min(cumulvax$vax1_date), "month"), max(cumulvax$vax1_date)+1,by=14),
    limits = c(lubridate::floor_date(min(cumulvax$vax1_date), "1 month"), NA),
    labels = scales::date_format("%d/%m"),
    expand = expansion(0),
    sec.axis = sec_axis(
      trans = ~as.Date(.),
      breaks=as.Date(seq(floor_date(min(cumulvax$vax1_date), "month"), ceiling_date(max(cumulvax$vax1_date), "month"),by="month")),
      labels = scales::date_format("%b %y")
    )
  )+
  scale_fill_brewer(type="qual", palette="Set2")+
  labs(
    x="Date",
    y="Vaccinated, n",
    colour=NULL,
    fill=NULL,
    alpha=NULL
  ) +
  theme_minimal()+
  theme(
    axis.text.x.top=element_text(hjust=0),
    axis.ticks.x.top=element_line(),
    strip.text.y=element_text(angle=0),
    legend.position = "bottom",

  )


plot_step <-
  ggplot(cumulvax)+
  geom_step(
    aes(
      x=vax1_date+1, y=cumuln,
      group=vax1_type_descr,
      colour=vax1_type_descr
    )
  )+
  scale_x_date(
    breaks = seq(floor_date(min(cumulvax$vax1_date), "month"), max(cumulvax$vax1_date)+1,by=14),
    limits = c(lubridate::floor_date((min(cumulvax$vax1_date)), "1 month"), NA),
    labels = scales::date_format("%d/%m"),
    expand = expansion(0),
    sec.axis = sec_axis(
      trans = ~as.Date(.),
      breaks=as.Date(seq(floor_date(min(cumulvax$vax1_date), "month"), ceiling_date(max(cumulvax$vax1_date), "month"),by="month")),
      labels = scales::date_format("%b %y")
    )
  )+
  scale_colour_brewer(type="qual", palette="Set2")+
  labs(
    x="Date",
    y="Vaccinated, n",
    colour=NULL,
    fill=NULL,
    alpha=NULL
  ) +
  theme_minimal()+
  theme(
    axis.text.x.top=element_text(hjust=0),
    axis.ticks.x.top=element_line(),
    legend.position = "bottom"
  )


write_rds(plot_step, here("output", "vaxdate", "plot_vaxdate_step_jcvi.rds"))
write_rds(plot_stack, here("output", "vaxdate", "plot_vaxdate_stack_jcvi.rds"))

ggsave(plot_step, filename="plot_vaxdate_step_jcvi.png", path=here("output", "vaxdate"))
ggsave(plot_stack, filename="plot_vaxdate_stack_jcvi.png", path=here("output", "vaxdate"))

