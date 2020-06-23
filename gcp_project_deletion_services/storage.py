class storage:

    def storage_list(self,project_id):
        
        from gcp_project_deletion_services.variable import resource_manager_service

        get_project_request = resource_manager_service.projects().get(projectId=project_id)

        get_project_response = get_project_request.execute()

        project_number = get_project_response.get('projectNumber')

        storage_api = "storage-component.googleapis.com"

        from gcp_project_deletion_services.variable import service_usage_service

        request = service_usage_service.services().get(
            name="projects/" + project_number + "/services/" + storage_api)

        response = request.execute()

        storage_api_status = response.get('state')

        if storage_api_status == 'DISABLED':

            endpoint_enable_request = service_usage_service.services().enable(name="projects/" + project_number + "/services/" + storage_api)

            endpoint_enable_response = endpoint_enable_request.execute()

        from gcp_project_deletion_services.variable import storage_client

        storage_list = list(storage_client.list_buckets(project=project_id))

        if len(storage_list)>0:

            for storage_name in storage_list:

                storage_deletion = storage_client.get_bucket(storage_name.name)

                storage_deletion.delete()

        storage_exist = False

        return storage_exist










