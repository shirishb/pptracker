## Models

### Version History

| Version | Note |
| --- | --- |
| 0.1 | Creation Project, Activity |


### Project

| Attribute | Type | Validation rules | Notes |
| --- | --- | --- | --- |
| id | Integer | Primary key | |
| tag | String(40) | Unique, lower case alphabet only (a-z) |  |
| name | String(80) | Not null | |
| date_started | Date | Null or Date <= today | |
| date_finished | Date | Null or Date <= today | |
| priority | Integer| \[0-255\] | |
| activities | | | 1..many Activity |
| type | Enum | | |
| isbn | | | | Applies to books only |

### Activity
| Attribute | Type | Validation rules | Notes |
| --- | --- | --- | --- |
| id | Integer | Primary key | |
| project_id | Integer | Foreign key | |
| description | String (80) | Not null | |
| date_started | Date | Null or Date <= today | |
| date_finished | Date | Null or Date <= today | |
| priority | Integer| 0-255 | |
| type | Enum | | |
| int_data | Integer | None | Type specific integer value |
| string_data | String(255) | None | Type specific string value |
| date_planned | Date | Date >= today, data_started = date_finished = NULL | |
| estimated_days | Integer | Null or >=0 | |


