from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class MjutilsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import mj.utils
        xmlconfig.file(
            'configure.zcml',
            mj.utils,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mj.utils:default')

MJ_UTILS_FIXTURE = MjutilsLayer()
MJ_UTILS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MJ_UTILS_FIXTURE,),
    name="MjutilsLayer:Integration"
)
MJ_UTILS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MJ_UTILS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="MjutilsLayer:Functional"
)
