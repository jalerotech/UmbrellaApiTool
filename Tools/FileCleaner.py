import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def cleanFile(file_path):
    """
    Cleans up the results.json file.
    :param file_path:
    :return: None
    """
    logger = logging.getLogger("File cleaner")
    file_name = file_path.split('/')[1]
    with open(file_path, 'w') as json_file:
        logger.info(f"{file_name} opened")
        logger.info(f'Cleaning up {file_name} file')
        json_file.close()
        logger.info(f'{file_name} file cleaned \n ')
