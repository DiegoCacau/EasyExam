from config.models import Config


def get(name):

    try:
        return Config.get(name)
    except Config.DoesNotExist as e:
        raise Exception('There is no parameter named ' + name + ' in the'
                        ' database')
