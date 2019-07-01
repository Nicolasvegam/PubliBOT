import tableauserverclient as TSC
import cv2 #Cropping

## Tableau connection - Credentials
class Tableau_extractor:

    def __init__(self):
        self.tableau_auth = TSC.TableauAuth('public', 'public', site_id='Sales') # username/password/sitio
        self.server = TSC.Server('https://tableau.adminml.com') #Server
        self.server.version = '2.5' #Changing version
        self.server.use_server_version()
        self.working_data = []


    def get_images(self, seller):

        with self.server.auth.sign_in(self.tableau_auth):

            all_views, pagination_item = self.server.views.get() # Get all views in Sales site
            all_project_items, pagination_item = self.server.projects.get() #Get all projects in Sales site
            all_workbooks, pagination_item = self.server.workbooks.get() #Get all workbooks in Sales site

            #Making filters
            req_option = TSC.RequestOptions()
            req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                             TSC.RequestOptions.Operator.Equals,
                                             'Seller Detail'))
            matching_views, pagination_item = self.server.views.get(req_option)

            #Finding the right view: Seller_Details/MLC Daily View - Seller_Details/MLC Montly View
            real_matching_views = []
            for view in matching_views:
                workbook = self.server.workbooks.get_by_id(view.workbook_id)
                if workbook.name == "MLC Daily View" or workbook.name == "MLC Monthly View":
                    real_matching_views.append(view)
                    print(view.name + ": " + workbook.name)

            Monthly_view = real_matching_views[0]
            Daily_view = real_matching_views[1]

            #Adding filter views
            #Seller filter -> done
            #Date range filter -> not yet -> not found *solution: create a new view with our date range

            montly_option_factory = getattr(TSC, "ImageRequestOptions")
            montly_options = montly_option_factory().vf("Seller Name", seller)
            daily_option_factory = getattr(TSC, "ImageRequestOptions")
            daily_options = daily_option_factory().vf("SELLER_NAME", seller)

            #---------Pendiente------------
            daily_options = daily_option_factory().vf("WINNING_DATE","2019/03/20-2019/03/27")
            #---------Pendiente------------

            self.server.views.populate_image(Monthly_view, montly_options)
            self.server.views.populate_image(Daily_view, daily_options)

            with open('./{0}_monthly_view.png'.format(seller), 'wb') as f:
                   f.write(Monthly_view.image)
            with open('./{0}_daily_view.png'.format(seller), 'wb') as f:
                   f.write(Daily_view.image)

    def cropping_images(self, seller):

        montly_img = cv2.imread("{0}_monthly_view.png".format(seller))
        daily_img = cv2.imread("{0}_daily_view.png".format(seller))
        crop_montly_img = montly_img[175:1500, 0:800] #Cropping in the right size, just required insights
        crop_daily_img = daily_img[250:1075, 0:800] #Cropping in the right size, just required insights

        cv2.imwrite("{0}_monthly_view.png".format(seller), crop_montly_img)
        cv2.imwrite("{0}_daily_view.png".format(seller), crop_daily_img)
        cv2.waitKey(0)


#if __name__ == '__main__':
#    seller = "SOMELASA"
#    class_ = Tableau_extractor()
#    class_.get_images(seller)
#    class_.cropping_images(seller)
#First part done