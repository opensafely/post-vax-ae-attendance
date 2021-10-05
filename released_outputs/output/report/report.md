---
title: "Post-vaccination Accident and Emergency Department Attendances"
output:
  html_document:
    keep_md: yes
  #  keep_html: TRUE
  #  code_folding: hide
  #  keep_md: yes
  #pdf_document: default
  #md_document:
  #   variant: gfm
  #github_document
---



# Introduction

Three vaccines have been used as part of the national COVID-19 vaccination programme in England to date: Pfizer-BioNTech BNT162b2 mRNA (*BNT162b2*), Oxford-AstraZeneca ChAdOx1 nCoV-19 (*ChAdOx1*), and Moderna mRNA-1273 (*Moderna*). This report describes rates of attendances to accident and emergency departments (A&E) in the first 2 weeks following the first recorded dose of these vaccines. 

The code and data for this report can be found at the OpenSafely [post-vax-ae-attendances GitHub repository](https://github.com/opensafely/post-vax-ae-attendances). 


# Methods

People meeting the following criteria are included:

* People receiving their first vaccine dose as part of the national COVID-19 vaccination programme (i.e., not administered in clinical trials):
  * BNT162b2 received on or after 08 December 2020;
  * ChAdOx1 received on or after 04 January 2021;
  * Moderna received on or after 07 April 2021.
* Vaccinated on or before 01 August 2021
* Registered at a GP practice using TPP's SystmOne clinical information system on the day before vaccination.
* Aged 16 or over.

The vaccination brand is available in the GP record directly, via the National Immunisation Management System (NIMS).

A&E attendances are identified using linked data from the Emergency Care Data Set (ECDS) provided by NHS Digital's Secondary Use Service (SUS), which holds records on all attendances to A&E departments. For each A&E attendance, one or more diagnosis codes are recorded. These have been categorised into 21 categories, as follows: Anaphylaxis, drug reaction; Cardiac, circulatory; COVID-19; Deprecated; Gastointestinal; Gynae; head and neck; Infection; Endocrine, metabolic; Haemaological; Neurological; Musculoskeletal, skin, rheumatic, allergy; No abnormality detected; Obstetric; Paediatric; Psychiachtric, toxicology, substance abuse; Renal, urological; Respiratory; Other vascular; Thromboembolic; Enviromental, Social, trauma.

Vaccine recipients are classified into one of the [10 vaccine priority groups defined by the Joint Committee on Vaccination and Immunisation (JCVI)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1007737/Greenbook_chapter_14a_30July2021.pdf#page=12) expert working group. These are based on demographic, clinical, or occupational characteristics identified on or before the vaccination date, except for age, which is determined as of 31 March 2020. These are:

1. Residents in a care home for older adults; Staff working in care homes for older adults
2. All those 80 years of age and over; Frontline health and social care workers
3. All those 75 years of age and over
4. All those 70 years of age and over; Individuals aged 16 to 69 in a high risk group
5. All those 65 years of age and over
6. Adults aged 16 to 65 years in an at-risk group
7. All those 60 years of age and over
8. All those 55 years of age and over
9. All those 50 years of age and over
10. Everybody else.

# Results

Note all counts below 6 are redacted and survival estimates are rounded for disclosure control.

## Characteristics as at vaccination date

<!--html_preserve--><style>html {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
}

#mmcauwkggx .gt_table {
  display: table;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#mmcauwkggx .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#mmcauwkggx .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#mmcauwkggx .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 0;
  padding-bottom: 4px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#mmcauwkggx .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#mmcauwkggx .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#mmcauwkggx .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#mmcauwkggx .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#mmcauwkggx .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#mmcauwkggx .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#mmcauwkggx .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#mmcauwkggx .gt_group_heading {
  padding: 8px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
}

#mmcauwkggx .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#mmcauwkggx .gt_from_md > :first-child {
  margin-top: 0;
}

#mmcauwkggx .gt_from_md > :last-child {
  margin-bottom: 0;
}

#mmcauwkggx .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#mmcauwkggx .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 12px;
}

#mmcauwkggx .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#mmcauwkggx .gt_first_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
}

#mmcauwkggx .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#mmcauwkggx .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#mmcauwkggx .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#mmcauwkggx .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#mmcauwkggx .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#mmcauwkggx .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding: 4px;
}

#mmcauwkggx .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#mmcauwkggx .gt_sourcenote {
  font-size: 90%;
  padding: 4px;
}

#mmcauwkggx .gt_left {
  text-align: left;
}

#mmcauwkggx .gt_center {
  text-align: center;
}

#mmcauwkggx .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#mmcauwkggx .gt_font_normal {
  font-weight: normal;
}

#mmcauwkggx .gt_font_bold {
  font-weight: bold;
}

#mmcauwkggx .gt_font_italic {
  font-style: italic;
}

#mmcauwkggx .gt_super {
  font-size: 65%;
}

#mmcauwkggx .gt_footnote_marks {
  font-style: italic;
  font-size: 65%;
}
</style>
<div id="mmcauwkggx" style="overflow-x:auto;overflow-y:auto;width:auto;height:auto;"><table class="gt_table">
  
  <thead class="gt_col_headings">
    <tr>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1"><strong>Characteristic</strong></th>
      <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1"><strong>BNT162b2</strong>, N = 7,003,980</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1"><strong>ChAdOx1</strong>, N = 8,528,673</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1"><strong>Moderna</strong>, N = 383,723</th>
    </tr>
  </thead>
  <tbody class="gt_table_body">
    <tr>
      <td class="gt_row gt_left">Age</td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">under 18</td>
      <td class="gt_row gt_center">44,945 (0.6%)</td>
      <td class="gt_row gt_center">3,996 (&lt;0.1%)</td>
      <td class="gt_row gt_center">56 (&lt;0.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">18-50</td>
      <td class="gt_row gt_center">3,975,284 (57%)</td>
      <td class="gt_row gt_center">2,893,605 (34%)</td>
      <td class="gt_row gt_center">376,691 (98%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">50-54</td>
      <td class="gt_row gt_center">304,295 (4.3%)</td>
      <td class="gt_row gt_center">1,192,430 (14%)</td>
      <td class="gt_row gt_center">3,391 (0.9%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">55-59</td>
      <td class="gt_row gt_center">337,813 (4.8%)</td>
      <td class="gt_row gt_center">1,152,507 (14%)</td>
      <td class="gt_row gt_center">1,748 (0.5%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">60-64</td>
      <td class="gt_row gt_center">348,848 (5.0%)</td>
      <td class="gt_row gt_center">959,891 (11%)</td>
      <td class="gt_row gt_center">897 (0.2%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">65-69</td>
      <td class="gt_row gt_center">379,077 (5.4%)</td>
      <td class="gt_row gt_center">755,036 (8.9%)</td>
      <td class="gt_row gt_center">462 (0.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">70-74</td>
      <td class="gt_row gt_center">412,448 (5.9%)</td>
      <td class="gt_row gt_center">762,788 (8.9%)</td>
      <td class="gt_row gt_center">265 (&lt;0.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">75-79</td>
      <td class="gt_row gt_center">397,750 (5.7%)</td>
      <td class="gt_row gt_center">454,212 (5.3%)</td>
      <td class="gt_row gt_center">118 (&lt;0.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">80+</td>
      <td class="gt_row gt_center">803,520 (11%)</td>
      <td class="gt_row gt_center">354,208 (4.2%)</td>
      <td class="gt_row gt_center">95 (&lt;0.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left">Sex</td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Female</td>
      <td class="gt_row gt_center">3,728,592 (53%)</td>
      <td class="gt_row gt_center">4,356,595 (51%)</td>
      <td class="gt_row gt_center">167,512 (44%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Male</td>
      <td class="gt_row gt_center">3,275,199 (47%)</td>
      <td class="gt_row gt_center">4,171,945 (49%)</td>
      <td class="gt_row gt_center">216,193 (56%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Unknown</td>
      <td class="gt_row gt_center">189</td>
      <td class="gt_row gt_center">133</td>
      <td class="gt_row gt_center">18</td>
    </tr>
    <tr>
      <td class="gt_row gt_left">Ethnicity</td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">White</td>
      <td class="gt_row gt_center">5,525,986 (87%)</td>
      <td class="gt_row gt_center">7,004,352 (90%)</td>
      <td class="gt_row gt_center">284,722 (86%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Black</td>
      <td class="gt_row gt_center">114,879 (1.8%)</td>
      <td class="gt_row gt_center">138,228 (1.8%)</td>
      <td class="gt_row gt_center">7,804 (2.4%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">South Asian</td>
      <td class="gt_row gt_center">480,538 (7.6%)</td>
      <td class="gt_row gt_center">470,590 (6.0%)</td>
      <td class="gt_row gt_center">20,659 (6.3%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Mixed</td>
      <td class="gt_row gt_center">77,348 (1.2%)</td>
      <td class="gt_row gt_center">70,027 (0.9%)</td>
      <td class="gt_row gt_center">6,299 (1.9%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Other</td>
      <td class="gt_row gt_center">137,068 (2.2%)</td>
      <td class="gt_row gt_center">124,369 (1.6%)</td>
      <td class="gt_row gt_center">10,072 (3.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Unknown</td>
      <td class="gt_row gt_center">668,161</td>
      <td class="gt_row gt_center">721,107</td>
      <td class="gt_row gt_center">54,167</td>
    </tr>
    <tr>
      <td class="gt_row gt_left">IMD</td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">1 most deprived</td>
      <td class="gt_row gt_center">1,166,583 (17%)</td>
      <td class="gt_row gt_center">1,413,210 (17%)</td>
      <td class="gt_row gt_center">67,090 (18%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">2</td>
      <td class="gt_row gt_center">1,326,817 (19%)</td>
      <td class="gt_row gt_center">1,567,605 (19%)</td>
      <td class="gt_row gt_center">68,970 (19%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">3</td>
      <td class="gt_row gt_center">1,496,394 (22%)</td>
      <td class="gt_row gt_center">1,820,403 (22%)</td>
      <td class="gt_row gt_center">82,532 (22%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">4</td>
      <td class="gt_row gt_center">1,455,864 (21%)</td>
      <td class="gt_row gt_center">1,798,785 (22%)</td>
      <td class="gt_row gt_center">79,414 (21%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">5 least deprived</td>
      <td class="gt_row gt_center">1,358,980 (20%)</td>
      <td class="gt_row gt_center">1,733,303 (21%)</td>
      <td class="gt_row gt_center">73,591 (20%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Unknown</td>
      <td class="gt_row gt_center">199,342</td>
      <td class="gt_row gt_center">195,367</td>
      <td class="gt_row gt_center">12,126</td>
    </tr>
    <tr>
      <td class="gt_row gt_left">Region</td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">North East and Yorkshire</td>
      <td class="gt_row gt_center">1,274,221 (18%)</td>
      <td class="gt_row gt_center">1,633,457 (19%)</td>
      <td class="gt_row gt_center">86,626 (23%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Midlands</td>
      <td class="gt_row gt_center">1,466,778 (21%)</td>
      <td class="gt_row gt_center">1,841,365 (22%)</td>
      <td class="gt_row gt_center">39,482 (10%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">North West</td>
      <td class="gt_row gt_center">634,974 (9.1%)</td>
      <td class="gt_row gt_center">773,548 (9.1%)</td>
      <td class="gt_row gt_center">22,642 (5.9%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">East of England</td>
      <td class="gt_row gt_center">1,596,151 (23%)</td>
      <td class="gt_row gt_center">2,017,743 (24%)</td>
      <td class="gt_row gt_center">109,091 (28%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">London</td>
      <td class="gt_row gt_center">485,886 (6.9%)</td>
      <td class="gt_row gt_center">421,288 (4.9%)</td>
      <td class="gt_row gt_center">23,607 (6.2%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">South East</td>
      <td class="gt_row gt_center">461,671 (6.6%)</td>
      <td class="gt_row gt_center">597,785 (7.0%)</td>
      <td class="gt_row gt_center">52,598 (14%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">South West</td>
      <td class="gt_row gt_center">1,081,462 (15%)</td>
      <td class="gt_row gt_center">1,240,889 (15%)</td>
      <td class="gt_row gt_center">49,603 (13%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">Unknown</td>
      <td class="gt_row gt_center">2,837</td>
      <td class="gt_row gt_center">2,598</td>
      <td class="gt_row gt_center">74</td>
    </tr>
    <tr>
      <td class="gt_row gt_left">Day of vaccination</td>
      <td class="gt_row gt_center">80 (47, 183)</td>
      <td class="gt_row gt_center">93 (66, 107)</td>
      <td class="gt_row gt_center">186 (166, 204)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left">JCVI priority group</td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
      <td class="gt_row gt_center"></td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">1 &amp; 2</td>
      <td class="gt_row gt_center">1,143,437 (16%)</td>
      <td class="gt_row gt_center">486,971 (5.7%)</td>
      <td class="gt_row gt_center">2,683 (0.7%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">3</td>
      <td class="gt_row gt_center">397,876 (5.7%)</td>
      <td class="gt_row gt_center">386,881 (4.5%)</td>
      <td class="gt_row gt_center">108 (&lt;0.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">4</td>
      <td class="gt_row gt_center">648,793 (9.3%)</td>
      <td class="gt_row gt_center">1,166,013 (14%)</td>
      <td class="gt_row gt_center">1,564 (0.4%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">5</td>
      <td class="gt_row gt_center">330,792 (4.7%)</td>
      <td class="gt_row gt_center">665,225 (7.8%)</td>
      <td class="gt_row gt_center">375 (&lt;0.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">6</td>
      <td class="gt_row gt_center">575,557 (8.2%)</td>
      <td class="gt_row gt_center">1,004,820 (12%)</td>
      <td class="gt_row gt_center">7,452 (1.9%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">7</td>
      <td class="gt_row gt_center">152,458 (2.2%)</td>
      <td class="gt_row gt_center">615,663 (7.2%)</td>
      <td class="gt_row gt_center">559 (0.1%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">8</td>
      <td class="gt_row gt_center">139,331 (2.0%)</td>
      <td class="gt_row gt_center">841,026 (9.9%)</td>
      <td class="gt_row gt_center">1,141 (0.3%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">9</td>
      <td class="gt_row gt_center">136,990 (2.0%)</td>
      <td class="gt_row gt_center">940,053 (11%)</td>
      <td class="gt_row gt_center">1,977 (0.5%)</td>
    </tr>
    <tr>
      <td class="gt_row gt_left" style="text-align: left; text-indent: 10px;">10</td>
      <td class="gt_row gt_center">3,478,746 (50%)</td>
      <td class="gt_row gt_center">2,422,021 (28%)</td>
      <td class="gt_row gt_center">367,864 (96%)</td>
    </tr>
  </tbody>
  
  
</table></div><!--/html_preserve-->


## Vaccination dates


### Overall
<img src="/workspace/output/report/figures/vaxdate-1.png" width="80%" />  

<!-- ### By JCVI priority group -->

<!-- ```{r, vaxdate_jcvi, echo=FALSE, message=FALSE, warning=FALSE, out.width='80%', fig.height=8, results='asis'} -->
<!--   vaxdate_plot <- read_rds(here("output", "vaxdate", "plot_vaxdate_stack_jcvi.rds")) -->
<!--   print(vaxdate_plot) -->
<!--   cat("  \n\n") -->
<!-- ``` -->

## Accident and Emergency attendance

### Overall

<img src="/workspace/output/report/figures/surv-1.png" width="80%" />  

### Diagnosis-specific attendances

####  Anaphylaxis, drug reaction  

<img src="/workspace/output/report/figures/surv_diagnosis-1.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-2.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-3.png" width="80%" />  

####  Cardiac, circulatory  

<img src="/workspace/output/report/figures/surv_diagnosis-4.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-5.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-6.png" width="80%" />  

####  COVID-19  

<img src="/workspace/output/report/figures/surv_diagnosis-7.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-8.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-9.png" width="80%" />  

####  Deprecated  

<img src="/workspace/output/report/figures/surv_diagnosis-10.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-11.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-12.png" width="80%" />  

####  Gastointestinal  

<img src="/workspace/output/report/figures/surv_diagnosis-13.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-14.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-15.png" width="80%" />  

####  Gynae  

<img src="/workspace/output/report/figures/surv_diagnosis-16.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-17.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-18.png" width="80%" />  

####  head and neck  

<img src="/workspace/output/report/figures/surv_diagnosis-19.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-20.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-21.png" width="80%" />  

####  Infection  

<img src="/workspace/output/report/figures/surv_diagnosis-22.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-23.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-24.png" width="80%" />  

####  Endocrine, metabolic  

<img src="/workspace/output/report/figures/surv_diagnosis-25.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-26.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-27.png" width="80%" />  

####  Haemaological  

<img src="/workspace/output/report/figures/surv_diagnosis-28.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-29.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-30.png" width="80%" />  

####  Neurological  

<img src="/workspace/output/report/figures/surv_diagnosis-31.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-32.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-33.png" width="80%" />  

####  Musculoskeletal, skin, rheumatic, allergy  

<img src="/workspace/output/report/figures/surv_diagnosis-34.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-35.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-36.png" width="80%" />  

####  No abnormality detected  

<img src="/workspace/output/report/figures/surv_diagnosis-37.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-38.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-39.png" width="80%" />  

####  Obstetric  

<img src="/workspace/output/report/figures/surv_diagnosis-40.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-41.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-42.png" width="80%" />  

####  Paediatric  

<img src="/workspace/output/report/figures/surv_diagnosis-43.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-44.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-45.png" width="80%" />  

####  Psychiachtric, toxicology, substance abuse  

<img src="/workspace/output/report/figures/surv_diagnosis-46.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-47.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-48.png" width="80%" />  

####  Renal, urological  

<img src="/workspace/output/report/figures/surv_diagnosis-49.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-50.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-51.png" width="80%" />  

####  Respiratory  

<img src="/workspace/output/report/figures/surv_diagnosis-52.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-53.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-54.png" width="80%" />  

####  Other vascular  

<img src="/workspace/output/report/figures/surv_diagnosis-55.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-56.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-57.png" width="80%" />  

####  Thromboembolic  

<img src="/workspace/output/report/figures/surv_diagnosis-58.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-59.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-60.png" width="80%" />  

####  Enviromental, Social, trauma  

<img src="/workspace/output/report/figures/surv_diagnosis-61.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-62.png" width="80%" />  

<img src="/workspace/output/report/figures/surv_diagnosis-63.png" width="80%" />  





