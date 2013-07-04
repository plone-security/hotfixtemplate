Plone Hotfix, 2013-XX-XX
========================

This hotfix fixes multiple vulnerabilities in Plone,
including arbitrary code execution and privilege escalation.

This hotfix should be applied to the following versions of Plone:

# Plone XX <= XX
* Plone XX <= XX


The hotfix is officially supported by the Plone security team on the
following versions of Plone in accordance with the Plone
`version support policy`_: 3.3.6, 4.1.6, and 4.2.2.
However it has also received some testing on older versions of Plone.
The fixes included here will be incorporated into subsequent releases of Plone,
so Plone XXX, XXX and greater should not require this hotfix.


Installation
============

Installation instructions can be found at
http://plone.org/products/plone-hotfix/releases/20130611


Q&A
===

Q: How can I confirm that the hotfix is installed correctly and my site is protected?
  A: On startup, the hotfix will log a number of messages to the Zope event log
  that look like this::

    2013-11-05 21:15:26 INFO Products.PloneHotfix2013XXXX Applied foo patch

  The exact list of patches attempted depends on the version of Plone.
  If a patch is attempted but fails, it will be logged as a warning that says
  "Could not apply". This may indicate that you have a non-standard Plone
  installation.

Q: How can I report problems installing the patch?
  A: Contact the Plone security team at security@plone.org, or visit the
  #plone channel on freenode IRC.

Q: How can I report other potential security vulnerabilities?
  A: Please email the security team at security@plone.org rather than discussing
  potential security issues publicly.

.. _`version support policy`: http://plone.org/support/version-support-policy
