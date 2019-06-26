import tableauserverclient as TSC

tableau_auth = TSC.TableauAuth('public', 'public', site_id='Advertising')
server = TSC.Server('https://tableau.adminml.com')
#server.use_server_version()
#server.add_http_options({'verify': False})
working_data = []
with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    for datasource in all_datasources:
        if "PAds" in datasource.name:
            working_data.append(datasource)
        print(datasource.name)
    print("\nData de interés ")
    for element in working_data:
        print(element.name)
        server.datasources.download(element.id, filepath=None, no_extract=False)
