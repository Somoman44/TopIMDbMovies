# Analysis of Top 950 IMDB Rated Movies

This project performs an in-depth exploratory data analysis (EDA) on a dataset of the top 950 highest-rated movies from IMDb. The goal is to uncover patterns and relationships within the data, identify key contributors (directors, writers, stars), and understand the factors that contribute to a movie's high rating and ranking.

The analysis delves into data cleaning, visualization, and statistical exploration to draw meaningful conclusions about how movie ratings work and how they are ranked.

## 📊 Dataset

The dataset used in this project was obtained from **Kaggle** and is contained in the file `imdb-top-rated-movies-user-rated.csv`.

> MIT License
>
> Copyright (c) 2013 Mark Otto.
>
> Copyright (c) 2017 Andrew Fong.

It includes detailed information for each of the 950 movies, such as:
- `Title` and `Rank`
- `IMDb Rating` and `Votes`
- `Meta Score` (critic rating)
- `Worldwide Gross`
- `Director`, `Writers`, and `Stars`
- `Tags` (Genres) and `Description`

## 🛠️ Technologies Used

This analysis is conducted using Python and the following core data science libraries:
- **Pandas:** For data manipulation, cleaning, and aggregation.
- **NumPy:** For numerical operations.
- **Seaborn & Matplotlib:** For data visualization, including heatmaps, pair plots, and bar charts.

## 📈 Analysis Overview

The project is broken down into several key stages:

1.  **Data Loading and Initial Exploration**:
    - The dataset is loaded into a Pandas DataFrame.
    - Initial exploration is done using `.head()`, `.info()`, and `.describe()` to get a first look at the data structure, types, and summary statistics.

2.  **Data Cleaning and Preprocessing**:
    - **Votes Column:** Converted string values (e.g., `927K`, `1.2M`) into numerical integers.
    - **Worldwide Gross Column:** Cleaned and converted the string representations of currency (e.g., `$54-234-062`) into numerical float values, handling missing (`-`) and NaN entries.
    - **Categorical Columns:** Transformed comma-separated strings in `Tags`, `Stars`, and `Writers` into lists of individual items to facilitate counting and grouping.

3.  **Exploratory Data Analysis (EDA)**:
    - **Correlation Analysis**: A heatmap was generated to visualize the correlation between numerical features like `Rank`, `IMDb Rating`, `Meta Score`, and `Votes`.
    - **Pair Plot Visualization**: A pair plot was created to observe the pairwise relationships and distributions between all numerical variables.
    - **Top Contributors**: Identified and visualized the top 15 directors, writers, and stars who have the most movies featured in this high-rated list.
    - **Audience vs. Critic Ratings**: A comparative analysis of IMDb Ratings (audience) versus Meta Scores (critics) was performed. The difference between the scaled scores was analyzed to see whether the general audience agrees with professional critics.

## 💡 Key Findings

The analysis yielded several interesting insights:

* **Ranking Mechanism**: The dataset's `Rank` is inverted; a higher rank number corresponds to a better movie. `IMDb Rating` is the most significant factor in determining this rank.
* **Audience vs. Critics**:
    * On average, IMDb ratings (audience) and Meta Scores (critics) are in general agreement, with a mean difference close to zero.
    * The distribution shows that the general audience tends to overrate popular but critically middling films more than critics underrate niche, well-acclaimed films.
* **Top Performers**:
    * **Director**: Akira Kurosawa has the most films (11) on the list.
    * **Star**: Robert De Niro appears in the most films (14).
    * **Writer**: Hayao Miyazaki is the most prolific writer (10 films) in this dataset.
* **Key Metrics**:
    * The number of `Votes` has a positive correlation with `IMDb Rating`, suggesting that more popular films tend to receive higher ratings.
    * `Worldwide Gross` shows a positive correlation with `Votes`, which is expected as more viewers often translate to higher box office revenue.

## 🚀 How to Run This Project

### Prerequisites
Make sure you have Python 3.x installed. You will also need the following libraries, which can be installed via pip:
`pip install pandas numpy seaborn matplotlib jupyterlab`
### Steps
1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
2.  **Dataset**:
    - Download the `imdb-top-rated-movies-user-rated.csv` dataset.
    - Place it in the same directory as the Jupyter Notebook.
3.  **Launch Jupyter**:
    - Run Jupyter Notebook or JupyterLab:
    ```bash
    jupyter lab
    ```
    - Open the `project.ipynb` file.
4.  **Run the cells**:
    - Execute the cells sequentially to reproduce the analysis.
