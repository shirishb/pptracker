## Models

Project 1..many Activity

### Project

| Attribute | Type | Validation rules | Notes |
| --- | --- | --- | --- |
| id | Integer | Primary key | |
| tag | String(40) | Unique, lower case alphabet only (a-z) |  |
| name | String(80) | | |
| date_started | Date | Date <= today | |
| date_finished | Date | Date <= today | |
| priority | Integer| 0-255 | |
| activities | | | |
| type | Enum | | \"book\" |
| isbn | | | | Applies to books only |

### Activity
| Attribute | Type | Validation rules | Notes |
| --- | --- | --- | --- |
| id | Integer | Primary key | |
| project_id | Integer | Foreign key | |
| description | String (80) | | |
| date_started | Date | Date <= today | |
| date_finished | Date | Date <= today | |
| priority | Integer| 0-255 | |
| type | Enum | | \"link\" |
| int_data | Integer | | Type specific integer value |
| int_unit | String(16) | | |
| string_data | String | | Type specific string value |
| date_planned | Date | Date >= today, data_started = date_finished = NULL | |
| estimated_days | Integer | >=0 | |

## Version History

| Version | Note |
| --- | --- |
| 0.1 | Creation Project, Tasks |
