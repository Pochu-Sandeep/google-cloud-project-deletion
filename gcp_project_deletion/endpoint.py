class endpoint:

    def endpoint_list(self, project_id):

        endpoint_exist = False

        from gcp_project_deletion.variable import service_usage_service

        request = service_usage_service.services().list(parent="projects/"+project_id, filter='state:ENABLED')

        response = request.execute()

        for endpoint_details in response.get('services'):

            endpoint_list = endpoint_details.get('config','')

            endpoint_name = endpoint_list.get('name')

            if len(endpoint_name)>0:

                endpoint_exist = True

                break

        if endpoint_exist:

            print("Endpoints exists in project please delete")

        else:

            print("Endpoints doesn't exists in the project")

        return endpoint_exist

