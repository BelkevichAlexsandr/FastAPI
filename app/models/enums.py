from enum import (
    Enum,
    StrEnum,
)


class FixingTypeEnum(StrEnum):
    INTERMEDIATE_EXECUTION = "intermediate_execution"
    EDITING_TASK = "editing_task"
    COMPLETED = "completed"
    STOPPED = "stopped"


class SolutionTypeEnum(StrEnum):
    WITHOUT_CONSEQUENCES = "without_consequences"
    ROLLBACK = "rollback"
    WITH_DEVIATIONS = "with_deviations"
    DEFECT = "defect"


class TaskTypeStatus(Enum):
    OFFICIAL = "служебная"
    VOLUNTARY_PRESENTATION = "добровольное предъявление"
    AUTOMATIC = "автоматическая"


class TechnologyStatus(Enum):
    ACTIVE = "active"
    ALTERNATIVE = "alternative"
    DISABLE = "disable"


class FileType(Enum):
    CNCCP = "CNCCP"
    SKETCH = "SKETCH"
    MANUAL = "MANUAL"
    SAFETY = "SAFETY"


class DefectiveProductDefectCategoryEnum(StrEnum):
    MINOR = "Малозначительный"
    SIGNIFICANT = "Значительный"
    CRITICAL = "Критический"


class OrderTypeEnum(StrEnum):
    INNER = "inner"
    OUTER = "outer"
