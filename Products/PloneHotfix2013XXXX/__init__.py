import logging


logger = logging.getLogger('Products.PloneHotfix2013XXXX')


hotfixes = [
    'foo',
    ]


# Apply the fixes
for hotfix in hotfixes:
    try:
        __import__('Products.PloneHotfix2013XXXX.%s' % hotfix)
        logger.info('Applied %s patch' % hotfix)
    except:
        logger.warn('Could not apply %s' % hotfix)
logger.info('Hotfix installed')
