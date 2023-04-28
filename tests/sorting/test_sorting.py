from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 1000, "max_salary": 2100, "date_posted": "2020-08-15"},
        {"min_salary": 1350, "max_salary": 2500, "date_posted": "2021-08-16"},
        {"min_salary": 1600, "max_salary": 3700, "date_posted": "2022-08-17"},
        {"min_salary": 1800, "max_salary": 5000, "date_posted": "2023-08-18"},
    ]

    salary_min = [jobs[0], jobs[1], jobs[2], jobs[3]]
    salary_max = [jobs[3], jobs[2], jobs[1], jobs[0]]
    date_posted = [jobs[3], jobs[2], jobs[1], jobs[0]]

    sort_by(jobs, "min_salary")
    assert jobs == salary_min
    sort_by(jobs, "max_salary")
    assert jobs == salary_max
    sort_by(jobs, "date_posted")
    assert jobs == date_posted
