from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    read_csv = read(path)
    return max(
        [
            int(salary["max_salary"])
            for salary in read_csv
            if salary["max_salary"].isnumeric()
        ]
    )


# Em Python, isnumeric() é um método embutido usado para
#  manipulação de strings. O método issnumeric() retorna
# “True” se todos os caracteres da string forem numéricos,
# caso contrário, retorna “False”


def get_min_salary(path: str) -> int:
    read_csv = read(path)
    return min(
        [
            int(salary["min_salary"])
            for salary in read_csv
            if salary["min_salary"].isnumeric()
        ]
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    try:
        m_salary = job["min_salary"]
        mx_min_salary = job["max_salary"]
        if int(m_salary) > int(mx_min_salary):
            raise ValueError

        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])

    except TypeError:
        raise ValueError

    except KeyError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered = []

    for job in jobs:
        try:
            match = matches_salary_range(job, salary)
            if match:
                filtered.append(job)
        except ValueError:
            pass

    return filtered
