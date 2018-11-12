import os
from uuid import uuid4


def get_storage_path(filename, subdir):
    _, ext = os.path.splitext(filename)
    new_name = '{}{}'.format(str(uuid4()), ext)

    return os.path.join(subdir, new_name)
