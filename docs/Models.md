## Models

Project 1..many Activity

### Project

| Attribute | Type | Validation rules | Notes |
| --- | --- | --- | --- |
| id | Integer | Primary key | |
| tag | String(40) | Unique, lower case alphabet only (a-z) |  |
| name | String(80) | | |
| type | Enum | | |
| date_started | Date | Date <= today | |
| date_finished | Date | Date <= today | |
| priority | Integer| 0-255 | |
| isbn | | | | Applies to books only |
| activities | | | |

### Tasks
| Attribute | Type | Validation rules | Notes |
| --- | --- | --- | --- |
| id | Integer | Primary key | |
| project_id | Integer | Foreign key | |
| description | | | |
| date_started | Date | | |
| date_finished | Date | | |
| priority | Integer| 0-255 | |
| estimated_days | | | |
| http_url | String | | |
| date_visited | Date | | |
| summary | | | |

