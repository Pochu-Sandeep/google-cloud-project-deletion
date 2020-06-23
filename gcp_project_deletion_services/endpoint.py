class endpoint:

    def endpoint_list(self, project_id):
        
        from gcp_project_deletion_services.variable import resource_manager_service

        get_project_request = resource_manager_service.projects().get(projectId=project_id)

        get_project_response = get_project_request.execute()

        project_number = get_project_response.get('projectNumber')

        service_usage_api = "serviceusage.googleapis.com"

        from gcp_project_deletion_services.variable import service_usage_service

        request = service_usage_service.services().get(name="projects/" + project_number + "/services/" + service_usage_api)

        response = request.execute()

        storage_api_status = response.get('state')

        if storage_api_status == 'DISABLED':
            
            endpoint_enable_request = service_usage_service.services().enable(name="projects/" + project_number + "/services/" + service_usage_api)

            endpoint_enable_response = endpoint_enable_request.execute()

        from gcp_project_deletion_services.variable import service_usage_service

        request = service_usage_service.services().list(parent="projects/"+project_id, filter='state:ENABLED')

        response = request.execute()

        endpoint_details = response.get('services')

        try:

            while len(endpoint_details)>0:

                endpoint_name_list = [sub['name'] for sub in endpoint_details]

                for endpoint_name in endpoint_name_list:

                    try:

                        endpoint_disable_request = service_usage_service.services().disable(name=endpoint_name,body={"disableDependentServices":True})

                        endpoint_disable_response = endpoint_disable_request.execute()

                    except Exception:

                        continue

                request = service_usage_service.services().list(parent="projects/" + project_id, filter='state:ENABLED')

                response = request.execute()

                endpoint_details = response.get('services')

        except Exception:

            print("Endpoint doesn't exist")
            









