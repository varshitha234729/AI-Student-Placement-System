"""
Data Validation Utilities
"""

import re
from typing import Tuple, Optional


class Validators:
    """Collection of data validation methods."""
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """
        Validate email address format.
        
        Args:
            email: Email address to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
        
        if not email:
            return False, "Email is required"
        
        if len(email) > 100:
            return False, "Email is too long"
        
        if re.match(pattern, email):
            return True, ""
        
        return False, "Invalid email format"
    
    @staticmethod
    def validate_password(password: str) -> Tuple[bool, str]:
        """
        Validate password strength.
        
        Args:
            password: Password to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not password:
            return False, "Password is required"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        
        if len(password) > 50:
            return False, "Password is too long"
        
        return True, ""
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        """
        Validate student name.
        
        Args:
            name: Name to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not name:
            return False, "Name is required"
        
        if len(name) < 2:
            return False, "Name must be at least 2 characters"
        
        if len(name) > 100:
            return False, "Name is too long"
        
        if not re.match(r"^[a-zA-Z\\s\\'-]+$", name):
            return False, "Name contains invalid characters"
        
        return True, ""
    
    @staticmethod
    def validate_cgpa(cgpa: float) -> Tuple[bool, str]:
        """
        Validate CGPA value.
        
        Args:
            cgpa: CGPA to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            cgpa_float = float(cgpa)
        except (ValueError, TypeError):
            return False, "CGPA must be a number"
        
        if cgpa_float < 0 or cgpa_float > 10:
            return False, "CGPA must be between 0 and 10"
        
        return True, ""
    
    @staticmethod
    def validate_roll_number(roll_number: str) -> Tuple[bool, str]:
        """
        Validate roll number format.
        
        Args:
            roll_number: Roll number to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not roll_number:
            return False, "Roll number is required"
        
        if len(roll_number) < 2 or len(roll_number) > 20:
            return False, "Roll number format is invalid"
        
        return True, ""
    
    @staticmethod
    def validate_score(score: float, max_score: float = 100) -> Tuple[bool, str]:
        """
        Validate assessment score.
        
        Args:
            score: Score to validate
            max_score: Maximum possible score
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            score_float = float(score)
        except (ValueError, TypeError):
            return False, "Score must be a number"
        
        if score_float < 0 or score_float > max_score:
            return False, f"Score must be between 0 and {max_score}"
        
        return True, ""
    
    @staticmethod
    def validate_hours(hours: float) -> Tuple[bool, str]:
        """
        Validate practice hours.
        
        Args:
            hours: Hours to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            hours_float = float(hours)
        except (ValueError, TypeError):
            return False, "Hours must be a number"
        
        if hours_float < 0 or hours_float > 1000:
            return False, "Hours must be between 0 and 1000"
        
        return True, ""
    
    @staticmethod
    def validate_branch(branch: str) -> Tuple[bool, str]:
        """
        Validate branch/department.
        
        Args:
            branch: Branch to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        valid_branches = [
            "CSE",
            "IT",
            "ECE",
            "MECHANICAL",
            "CIVIL",
            "ELECTRICAL",
            "CHEMICAL",
            "OTHERS",
        ]
        
        if not branch:
            return False, "Branch is required"
        
        if branch.upper() not in valid_branches:
            return False, f"Invalid branch. Valid options: {', '.join(valid_branches)}"
        
        return True, ""
    
    @staticmethod
    def validate_all_fields(data: dict) -> Tuple[bool, str]:
        """
        Validate all required fields in a dictionary.
        
        Args:
            data: Dictionary of data to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        required_fields = ["name", "email", "cgpa", "roll_number", "branch"]
        
        for field in required_fields:
            if field not in data or not data[field]:
                return False, f"{field} is required"
        
        # Validate individual fields
        validators = [
            ("name", Validators.validate_name(data.get("name", ""))),
            ("email", Validators.validate_email(data.get("email", ""))),
            ("cgpa", Validators.validate_cgpa(data.get("cgpa", 0))),
            ("roll_number", Validators.validate_roll_number(data.get("roll_number", ""))),
            ("branch", Validators.validate_branch(data.get("branch", ""))),
        ]
        
        for field, (is_valid, error) in validators:
            if not is_valid:
                return False, error
        
        return True, ""
