class endpoint:

    def endpoint_list(self, project_id):

        from gcp_project_deletion.variable import service_usage_service

        request = service_usage_service.services().list(parent="projects/"+project_id, filter='state:ENABLED')

        response = request.execute()

        endpoint_details = response.get('services')

        #for len(endpoint_details)>0:

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

            endpoint_exist = False

        return endpoint_exist

obj_main = endpoint()

obj_main.endpoint_list("rare-ridge-279913")







