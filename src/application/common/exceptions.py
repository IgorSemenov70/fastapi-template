class ApplicationError(Exception):
    """
    Base class for application-specific exceptions.

    This class serves as the base for custom exceptions related to application errors.
    It can be used as a parent class for more specific exception classes.
    """

    @property
    def message(self) -> str:
        return "An application error occurred"


class UnexpectedError(ApplicationError):
    """
    Exception class representing unexpected application errors.
    This class represents unexpected errors that may occur during the application's execution.
    """


class CommitError(UnexpectedError):
    """
    Exception class for errors related to committing a transaction.
    This exception is raised when an error occurs during the process of committing a transaction.
    """


class RollbackError(UnexpectedError):
    """
    Exception class for errors related to rolling back a transaction.
    This exception is raised when an error occurs during the process of rolling back a transaction.
    """


class RepoError(UnexpectedError):
    """
    Custom exception class for repository-related errors.
    It is used to represent errors that occur specifically within a repository
    or data access layer.
    """
