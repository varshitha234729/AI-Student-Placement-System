"""
AI-Powered Student Placement Readiness System
Main package initialization
"""

__version__ = "1.0.0"
__author__ = "Varshitha"
__description__ = "AI-Powered Student Placement Readiness System"

from src.models.student import Student
from src.models.assessment import Assessment
from src.models.progress import ProgressTracker
from src.services.database_manager import DatabaseManager

__all__ = [
    "Student",
    "Assessment",
    "ProgressTracker",
    "DatabaseManager",
]
