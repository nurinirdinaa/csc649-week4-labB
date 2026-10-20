from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 3


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.
# TODO 1: days_left is negative when the task is overdue.
def test_is_negative_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)
    assert days_left(due, today) == -1
# TODO 2: is_urgent is True when the task is due tomorrow.
def test_is_urgent_when_due_tomorrow():
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)
    assert is_urgent(due, today) is True
# TODO 3: is_urgent is True when the task is due in exactly 2 days (the limit).
def test_is_urgent_when_due_limit():
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)
    assert is_urgent(due, today, limit=2) is True
# TODO 4: is_urgent is False when the task is overdue.
def test_is_not_urgent_when_task_due_in_future():
    today = date(2026, 10, 19)
    due = date(2026, 10, 15)
    assert is_urgent(due, today) is False
# TODO 5: sort_by_due puts the soonest task first.
def test_sort_by_due_puts_soonest_task_first():
    tasks = [
        {"due": date(2026, 10, 25)},
        {"due": date(2026, 10, 20)},
        {"due": date(2026, 10, 22)},
    ]
    sorted_tasks = sort_by_due(tasks)
    assert sorted_tasks[0]["due"] == date(2026, 10, 20)
# TODO 6: completion_rate returns 0.0 when there are no tasks.
def test_completion_rate_when_no_tasks():
    assert completion_rate(0,0) == 0.0
# TODO 7: completion_rate(1, 3) returns 33.3.
def test_completion_rate_when_rounds_to_one_decimal():
    assert completion_rate(1,3) == 33.3
