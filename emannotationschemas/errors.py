class UnknownAnnotationTypeException(Exception):
    """exception raised when an unknown schema is asked for"""


class InvalidTableMetaDataException(Exception):
    """exception is raised when metadata for a table is not valid or is missing"""


class InvalidSchemaField(Exception):
    """Exception raised if a schema can't be translated to a model"""


class VersionColumnsRequireSegmentationException(Exception):
    """Raised when with_version_columns=True is requested without a segmentation_source;
    the versioned anno_id/id/valid_from_version/valid_to_version restructuring only
    applies to segmentation tables."""
