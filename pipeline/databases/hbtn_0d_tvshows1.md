# Database hbtn_0d_tvshows Documentation

This database contains information about TV shows and their associated genres. It uses a many-to-many relationship structure.

## Entity-Relationship Diagram

```mermaid
erDiagram
    tv_shows {
        int id PK
        varchar(256) title
    }
    tv_genres {
        int id PK
        varchar(256) name
    }
    tv_show_genres {
        int show_id FK
        int genre_id FK
    }

    tv_shows ||--o{ tv_show_genres : "has"
    tv_genres ||--o{ tv_show_genres : "belongs to"
```
