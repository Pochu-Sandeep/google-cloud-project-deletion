class endpoint:

    def endpoint_list(self, project_id):

        from gcp_project_deletion.variable import service_usage_service

        request = service_usage_service.services().list(parent="projects/"+project_id, filter='state:ENABLED')

        response = request.execute()

        print(response)

        for endpoint_details in response.get('services'):

            endpoint_name = endpoint_details.get('name')

            print(endpoint_name)

            endpoint_disable_request = service_usage_service.services().disable(name=endpoint_name)

            endpoint_disable_response = endpoint_disable_request.execute()

        endpoint_exist = False

        return endpoint_exist

