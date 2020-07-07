class compute:

    def vm_list(self, project_id):
        
        from gcp_project_deletion_services.variable import resource_manager_service

        get_project_request = resource_manager_service.projects().get(projectId=project_id)

        get_project_response = get_project_request.execute()

        project_number = get_project_response.get('projectNumber')

        compute_engine_api = "compute.googleapis.com"

        from gcp_project_deletion_services.variable import service_usage_service

        request = service_usage_service.services().get(name="projects/" + project_number + "/services/" + compute_engine_api)

        response = request.execute()

        compute_engine_api_status = response.get('state')

        print(compute_engine_api_status)

        if compute_engine_api_status == 'DISABLED':

            endpoint_enable_request = service_usage_service.services().enable(name="projects/" + project_number + "/services/" + compute_engine_api)

            endpoint_enable_response = endpoint_enable_request.execute()

            print(endpoint_enable_response)

            time.sleep(600)

        from gcp_project_deletion_services.variable import service

        zone_request = service.zones().list(project=project_id)

        zone_response = zone_request.execute()

        for zone_details in zone_response['items']:

            zone_name = zone_details.get("name")

            instance_request = service.instances().list(project=project_id, zone=zone_name)

            instance_response = instance_request.execute()

            instance_details = instance_response.get("items", "")

            if len(instance_details) > 0:

                instance_name_list = [sub['name'] for sub in instance_details]

                for instance_name in instance_name_list:

                    instance_delete_request = service.instances().delete(project=project_id, zone=zone_name, instance=instance_name)

                    instance_delete_response = instance_delete_request.execute()

            instance_exist = False

        return instance_exist
















