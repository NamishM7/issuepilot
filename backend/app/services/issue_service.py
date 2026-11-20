from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID

from app.models.issue import Issue
from app.schemas.issue import IssueCreate, IssueResponse, IssueUpdate

def create_issue(db: Session, issue_data: IssueCreate):
    new_issue = Issue(
        title = issue_data.title,
        body = issue_data.body,
        repository = issue_data.repository,
        labels = issue_data.labels,
    )
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)

    return new_issue

def get_all_issues(db: Session):
    statement = select(Issue)
    result = db.scalars(statement)
    return result.all()

def get_issue_by_id(db: Session, issue_id: UUID):
    return db.get(Issue, issue_id)




# Update an existing issue
def update_issue(
    db: Session,
    issue_id: UUID,
    issue_data: IssueUpdate
):

    issue = db.get(Issue, issue_id)

    if issue is None:
        return None

    update_data = issue_data.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    for key, value in update_data.items():
        setattr(issue, key, value)

    try:
        db.commit()
        db.refresh(issue)
    except Exception:
        db.rollback()
        raise

    return issue


# Delete an existing issue
def delete_issue(db: Session, issue_id: UUID):

    issue = db.get(Issue, issue_id)

    if issue is None:
        return False

    try:
        db.delete(issue)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return True


























# from uuid import uuid4, UUID
# from datetime import datetime, timezone 

# from app.schemas.issue import IssueCreate, IssueResponse

# # temporary in-memory storage
# issues_db : dict[UUID, IssueResponse] = {}

# def create_issue(issue: IssueCreate) -> IssueResponse:
#     new_issue = IssueResponse(
#         id = uuid4(),
#         title = issue.title,
#         body = issue.body,
#         repository = issue.repository,
#         labels = issue.labels,
#         state = "open",
#         created_at = datetime.now(timezone.utc)
#     )

#     issues_db[new_issue.id] = new_issue
#     return new_issue

# def get_all_issues() -> list[IssueResponse]:
#     return list(issues_db.values())

# def get_issue_by_id(issue_id: UUID):
#     return issues_db.get(issue_id)


