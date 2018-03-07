from tethys_sdk.base import TethysAppBase, url_map_maker


class Distanceapp(TethysAppBase):
    """
    Tethys app class for Travel Time Distance Map App.
    """

    name = 'Travel Time Distance Map'
    index = 'distanceapp:home'
    icon = 'distanceapp/images/car.jpg'
    package = 'distanceapp'
    root_url = 'distanceapp'
    color = '#004225'
    description = 'This app shows how far vehicles can travel along any route through a road network in a given amount of time.'
    tags = '&quot;Transportation&quot;,&quot;Travel Times&quot;,&quot;Road Network&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='distanceapp',
                controller='distanceapp.controllers.home'
            ),
            UrlMap(
                name='mapview',
                url='distanceapp/mapview',
                controller='distanceapp.controllers.mapview'
            ),
            UrlMap(
                name='dataservices',
                url='distanceapp/dataservices',
                controller='distanceapp.controllers.dataservices'
            ),
            UrlMap(
                name='about',
                url='distanceapp/about',
                controller='distanceapp.controllers.about'
            ),
            UrlMap(
                name='proposal',
                url='distanceapp/proposal',
                controller='distanceapp.controllers.proposal'
            ),
            UrlMap(
                name='mockup',
                url='distanceapp/mockup',
                controller='distanceapp.controllers.mockup'
            ),
        )

        return url_maps


