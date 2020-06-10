class compute:

    def vm_list(self, project_id):

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
















