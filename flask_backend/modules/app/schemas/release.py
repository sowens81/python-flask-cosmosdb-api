from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

release_schema = {
    "type": "object",
    "properties": {
        "release_id": {
            "type": "string"
        },
        "release_artist": {
            "type": "string"
        },
        "release_name": {
            "type": "string"
        },
        "release_img_uri": {
            "type": "string"
        }
    },
    "required": ["release_id", "release_artist", "release_name", "release_img_uri"],
    "additionalProperties": False
}

def validate_release(data):
    try:
        validate(data, release_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}