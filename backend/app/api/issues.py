
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.database.connection import get_db

from app.schemas.issue import IssueCreate, IssueResponse, IssueUpdate

from app.services.issue_service import (
    create_issue,
    get_all_issues,
    get_issue_by_id,
    update_issue,
    delete_issue
)


router = APIRouter(
    prefix="/issues",
    tags=["Issues"]
)


# Create a new issue
@router.post(
    "/",
    response_model=IssueResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_issue(
    issue: IssueCreate,
    db: Session = Depends(get_db)
):

    return create_issue(db, issue)


# Retrieve all issues
@router.get("/", response_model=list[IssueResponse])
def retrieve_all_issues(
    db: Session = Depends(get_db)
):

    return get_all_issues(db)


# Retrieve a specific issue
@router.get("/{issue_id}", response_model=IssueResponse)
def retrieve_issue(
    issue_id: UUID,
    db: Session = Depends(get_db)
):

    issue = get_issue_by_id(db, issue_id)

    if issue is None:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    return issue

# Update an existing issue
@router.patch("/{issue_id}", response_model=IssueResponse)
def update_existing_issue(
    issue_id: UUID,
    issue_data: IssueUpdate,
    db: Session = Depends(get_db)
):

    issue = update_issue(db, issue_id, issue_data)

    if issue is None:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    return issue


# Delete an existing issue
@router.delete("/{issue_id}", status_code=204)
def delete_existing_issue(
    issue_id: UUID,
    db: Session = Depends(get_db)
):

    deleted = delete_issue(db, issue_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    return None
