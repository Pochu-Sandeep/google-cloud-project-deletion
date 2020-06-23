class storage:

    def storage_list(self,project_id):
        
        from gcp_project_deletion.variable import resource_manager_service

        get_project_request = resource_manager_service.projects().get(projectId=project_id)

        get_project_response = get_project_request.execute()

        project_number = get_project_response.get('projectNumber')

        storage_api = "storage-component.googleapis.com"

        from gcp_project_deletion.variable import service_usage_service

        request = service_usage_service.services().get(name="projects/" + project_number + "/services/" + storage_api)

        response = request.execute()

        storage_api_status = response.get('state')

        if storage_api_status == 'DISABLED':
            
            endpoint_enable_request = service_usage_service.services().enable(name="projects/" + project_number + "/services/" + storage_api)

            endpoint_enable_response = endpoint_enable_request.execute()

        storage_exist = False

        from gcp_project_deletion.variable import storage_client

        buckets = list(storage_client.list_buckets(project=project_id))

        if len(buckets)>0:

            print("Buckets exists in project please delete")

            storage_exist = True

        else:

            print("Buckets doesn't exists in the project")

        return storage_exist



