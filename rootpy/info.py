"""
                 _
 _ __ ___   ___ | |_ _ __  _   _
| '__/ _ \ / _ \| __| '_ \| | | |
| | | (_) | (_) | |_| |_) | |_| |
|_|  \___/ \___/ \__| .__/ \__, |
                    |_|    |___/
      %s
"""

from collections import namedtuple


_version_info_base = namedtuple('version_info',
                                ['major',
                                 'minor',
                                 'micro',
                                 'releaselevel',
                                 'serial'])


class version_info(_version_info_base):

    def __repr__(self):

        return 'rootpy.%s' % super(version_info, self).__repr__()

    def __str__(self):

        if self.releaselevel != 'final':
            return '%s.%s.%s-%s%s' % (self.major,
                                      self.minor,
                                      self.micro,
                                      self.releaselevel[0],
                                      self.serial)
        return '%s.%s.%s' % (self[:3])


__version_info__ = version_info(0, 7, 0, 'alpha', 0)
__version__ = str(__version_info__)
__url__ = 'http://rootpy.github.com/rootpy'
__repo_url__ = 'https://github.com/rootpy/rootpy/'
__download_url__ = ('http://pypi.python.org/packages/source/r/'
                    'rootpy/rootpy-%s.tar.gz') % __version__
__doc__ %= __version__
