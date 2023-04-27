from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path, encoding="utf-8") as file:
        read_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(read_csv)


print(read("./data/jobs.csv")[8])


def get_unique_job_types(path: str) -> List[str]:

    read_csv = read(path)
    jobs_types = [type["job_type"] for type in read_csv]
    return set(jobs_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:

    return [job for job in jobs if job["job_type"] == job_type]
