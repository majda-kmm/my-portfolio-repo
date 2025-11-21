# Beev - Integration & Data Analysis on the Automotive Market

## Repository Content

| File | Description |
|------|-------------|
| `docker-compose.yml` | Deploys a local PostgreSQL database using Docker. |
| `script.py` | Python script to read CSV files, create tables, and insert data into the database. |
| `car_data.csv` | Car data (model, engine type, price, year, etc.). |
| `consumer_data.csv` | Consumer rating data by country (volume, rating, etc.). |
| `requetes.sql` | SQL file containing the requested analytical queries. |
| `graph_bonus.py` | Generates two graphs (sales volume and value by engine type). |
| `volume_per_year.png` | Graph: annual sales volume (electric vs thermal). |
| `value_per_year.png` | Graph: annual sales value (electric vs thermal). |
| `jointure_resultat.csv` | Intermediate join result used for analysis. |

---

## Technical steps

### 1. Database setup
- Launch using `docker-compose up -d`
- Stop using `docker-compose down`
- Connect via pgAdmin if needed

### 2. Data insertion
- `script.py` reads both CSV files
- Creates tables and the necessary join
- Robust and automated data insertion

### 3. SQL queries (in `requetes.sql`)
- a. Total number of cars by model and country  
- b. Country with the most units of each model  
- c. Models sold in the USA but not in France  
- d. Average price by country and engine type  
- e. Average rating: electric vs thermal

### 4. Visualizations (bonus)
- `graph_bonus.py` generates two plots:
  - Annual sales volume (electric vs thermal)
  - Total annual sales value (price × volume)

---

## Technical choices

- **Flexible relational model**: I accounted for model variants over different years. Potential duplicates are filtered thoughtfully to retain only relevant versions for a given year.

- **Join based on `Make` only**:
  - The `Model` column in `consumer_data.csv` was often inconsistent.
  - To avoid incorrect or overly strict joins, I chose to **join only on the `Make` column**, assuming consumer ratings apply to all models of a brand at a given time.

- **Post-join temporal filtering**:
  - To ensure temporal consistency, only rows where `Production Year ≤ Review Year` are kept.
  - This ensures the model existed at the time of the evaluation.

- **Reasoned deduplication**:
  - When multiple versions of a model existed before a review, I kept **the version produced most recently before the review year**.
  - This better reflects market reality at the time of the evaluation.

- **Cleaning and standardizing string columns**:
  - I normalized all strings (`Make`, `Model`) by converting them to lowercase and stripping whitespace (`.str.strip().str.lower()`), to improve join quality.

---

## Execution guide

```bash
# Step 1: Start the database
docker-compose up -d

# Step 2: Load the data
python script.py

# Step 3: Run the SQL queries (via psql)
# Queries available in the file requetes.sql

# Step 4: Generate the graphs
python graph_bonus.py
```
