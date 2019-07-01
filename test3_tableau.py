import tableauserverclient as TSC

tableau_auth = TSC.TableauAuth('public', 'public', site_id='Advertising') # username/password/sitio
server = TSC.Server('https://tableau.adminml.com') #servidor
server.version = '2.5' # modificar la versión de la API
server.use_server_version()
working_data = []

with server.auth.sign_in(tableau_auth):

    #Sacando la dataSource de pAds
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    for datasource in all_datasources:
        if "PAds" in datasource.name:
            working_data.append(datasource)
        print(datasource.name)
    print("\nData de interés\n")
    for element in working_data:
        server.datasources.populate_connections(element)
        print(element.name)
        print(element.connections)
        # Esta es la función que descarga la base de datos localmente, no hay acceso con el usuario public-public
        #server.datasources.download(element.id, filepath=None, no_extract=False)

    #Sacando la views de pAds
    all_views, pagination_item = server.views.get()
    PAds_views = []
    number = 0
    for view in all_views:
        if "PAds" in view.name:
            number = number + 1
            print(view.name)
            PAds_views.append(view)
            server.views.populate_image(view)
            with open('./view{0}.png'.format(number), 'wb') as f:
	               f.write(view.image)
