import log
import re

logger = log.get_logger('validation')


def validation(field_name, field_val, type_id):
    types = [{66: {'type': int, 'min_len': 1, 'max_len': 15, 'reg': '^\d+?\d$'}},
             {72: {'type': str, 'min_len': 10, 'max_len': 12, 'reg': '(?s).*'}},  # # regex match with anything
             {91: {'type': str, 'min_len': 1, 'max_len': 1000000, 'reg': '(?s).*'}},  # ?????
             {92: {'type': str, 'min_len': 1, 'max_len': 1000000, 'reg': '(?s).*'}},  # ?????
             {100: {'type': str, 'min_len': 2, 'max_len': 4000, 'reg': '(?s).*'}},
             {128: {'type': str, 'min_len': 2, 'max_len': 4000, 'reg': '^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?'}},
             {130: {'type': int, 'min_len': 0, 'max_len': 1000000, 'reg': '(?s).*'}},
             {131: {'type': float, 'min_len': 0, 'max_len': 3, 'reg': '^\d+?\d$'}},
             {132: {'type': str, 'min_len': 2, 'max_len': 4000, 'reg': '(?s).*'}},
             {136: {'type': str, 'min_len': 0, 'max_len': 4, 'reg': '^\d+?\d$'}},
             {137: {'type': list, 'min_len': 0, 'max_len': 1000000, 'reg': '(?s).*'}},
             {140: {'type': list, 'min_len': 0, 'max_len': 1000000, 'reg': '(?s).*'}},
             {150: {'type': str, 'min_len': 2, 'max_len': 100, 'reg': '^\s*\D+\.?\D+\s*$'}},
             {159: {'type': str, 'min_len': 10, 'max_len': 1000, 'reg': '(?s).*'}},
             {160: {'type': str, 'min_len': 10, 'max_len': 1000, 'reg': '(?s).*'}},
             {161: {'type': str, 'min_len': 10, 'max_len': 1000, 'reg': '(?s).*'}},
             {162: {'type': str, 'min_len': 10, 'max_len': 1000, 'reg': '(?s).*'}},
             {240: {'type': str, 'min_len': 0, 'max_len': 20, 'reg': '(?s).*'}},
             {241: {'type': str, 'min_len': 0, 'max_len': 20, 'reg': '(?s).*'}},
             {244: {'type': str, 'min_len': 10, 'max_len': 1000000, 'reg': '(?s).*'}},
             {250: {'type': tuple, 'min_len': 0, 'max_len': 4000, 'reg': '(?s).*'}},
             ]
    for i in types:
        for k, v in i.items():
            if k == type_id:
                item = v

    if type(field_val) == item['type'] and item['min_len'] <= len(str(field_val)) <= item['max_len']:
        if re.match(item['reg'], str(field_val)):
            return field_val
    else:
        logger.info({field_name: field_val, 'type_id': type_id})
        return None


print(validation('Postal Code', '', 128))
