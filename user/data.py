class Data:
    def get_data(self, client_name):
        eca_data_cumulative = [
            ['64525a02-344c-4e12-b8fb-6ff54e82ddf6', 'dc861309-f38d-4754-8d9b-442f2b10743f', '214da7f6-eaa9-4e31-8709-83a3831b8e61'],
            ['4d75097a-dc07-4ea3-9e6b-3687eaea4416', '0e00e276-4619-4bdd-98bf-1ba087b84bfa', 'cc969b81-72c5-41c5-b00f-b8af2390946f'],
            ['6edfb82e-88fe-4a95-af70-3d8c6236d4ad', '07a04a43-ae3c-4bbc-a7cc-e42d757ccc68', 'f1f2a5e9-c4fd-4962-a652-6597986d163f'],
            ['62b9dca6-7503-43b2-af93-dbe3cb951118', 'e60fe9a8-495d-40b3-978b-e3227a761e43', '011cbe64-59d2-46b2-bf5a-c6a3567c3d34'],
            ['c858de97-2b21-4ab7-b6de-c4e00077c9a8', '52454aaf-4c91-4707-8d51-e2f974a69146', 'd94986bb-0033-45e7-8991-93106400f827'],
            ['7e45f2c4-7828-4b12-a405-f920c5974fb7', '490939d2-90af-4332-95a3-fb0d1a3f11bb', 'e6490009-8061-46d1-aa95-5d19b7a362e3'],
            ['3a6169f1-ed53-413f-87f0-2094e5824c65', '4be5ab4c-3f55-46e7-af43-a6312013fe29', '554b2c4e-f6e0-4b7f-8e70-d35c900738ff'],
            ['336376de-d6c1-449b-aa29-4e32a639c79b', '07c6cab2-64fc-4b81-adf6-0815fc45f1fb', 'f95a42e5-6ea5-4c15-b85b-d0248b4b440a'],
            ['bfe4b0a2-847f-4380-b73d-cfecb0238a44', '46f6f6eb-1e63-4054-bb9d-f4c407c1106a', 'e53fcb37-5042-4096-97b7-9bfdf1e8d082']
            ]

        eca_chart_data = [
            '9ccf70e1-4f25-4d26-b860-beadb06e6346', '63bde4be-a4c9-425d-9539-21b19408bc87', 'c4f2888c-67ab-44d7-af42-497c57dfaa57',
            '65a2c94d-c354-457e-858d-1da7861e937c'
            ]

        desert_orth_data_cumulative = [
            ['b3b3b3c0-4e68-442a-87bf-65cfac3c9b76', '39ab057d-3075-4b9c-a646-ff37debb4fb7', '98db6362-d30a-443c-a85f-1eb09367f9ba'],
            ['67aae50b-68ae-473f-8490-29c6e1af8bed', 'a2d3cbd0-3087-4e9c-ae38-8ecf37e1c8ab', '6d089972-c5fa-4ea5-a983-781b3263d0d0'],
            ['4b4f52bc-fa33-40f9-b2bf-a9c5af14f2b0', '759d8edc-16fd-4fa1-bd7f-5633dbb86be7', '0958e26e-2854-41e0-9369-13a23fa955af'],
            ['27a38399-f25c-42b4-95cd-e0ebb13113cb', '0fef0d59-7d22-469c-9fde-a4672e460a3e', '6e1d4f2a-b62c-4f87-aefc-03ffeb9348ef'],
            ['4ddcedbc-ed22-4420-b3b5-40b28bcd92d3', 'c1ef027f-e7c1-45d3-85e2-023c416d0969', '64c7dde6-3dfd-4fd8-a6d1-35004bac778a'],
            ['366817ce-71c8-45d6-ba4f-fd4065a115a9', '32a9f575-315e-4888-aac7-56f3a6fbe12f', '1683eb13-e20e-4e86-b4ec-e831b35f83cf'],
            ['fde8325b-d846-44ed-b620-e14088a6d41a', 'b5a110af-15d9-49dd-a0e1-676a962bbef7', '041310e9-a96b-469a-a084-6bbe8d311ab9'],
            ['fb7f08de-788c-4732-90be-a4b8119f9558', 'e51e2ab4-10e7-4044-b3db-2bb6226d3d82', '71c2b1c8-b590-4dc1-926e-89498fd35221'],
            ['25d182b1-07e5-4265-82f7-256e8c0e3df4', 'b3c96340-132b-4ec6-9c1a-21bf4c0867c4', '0d5d5d01-2a20-48a6-9b92-377954c8f023'],
        ]

        desert_orth_chart_data = [
            '7e77a7df-6ae5-47c6-8628-fcb332e20b8e', '89249536-aaee-4be0-9bb3-cc2650b504ac', '23fb0d2c-2bb1-401f-b356-2fdf462b54bc',
            '3d4cd7e8-2fe5-4c13-b5d3-437d23323fc8',
        ]

        manchester_data = [
            ['24125f75-0421-4787-8c3f-51d31bedc3c3', '4cef86e2-bc53-4231-8094-46fa0921f741', '99022590-d262-46a2-8621-a393284fc3c1'],
            ['8419f96a-99e9-4e64-b4c3-e351e00d69ed', '000b6a89-cb7b-434f-bf6c-3082ff985192', '158420bc-a870-40ce-b565-e61dd8b7bde5'],
            ['7116c484-228f-4457-9763-7737d1455b50', '0c697097-585a-46ad-b652-78a3186817c4', '634aff12-647f-441a-b326-f688820d1a25'],
            ['5afc102b-fff5-4e56-aea5-6790918e9081', '266073c2-1013-4091-8ce5-7142e5e5961f', '182591c7-45f9-4039-a75f-9d2a9fb9a1fe'],
            ['31d52675-1a0c-461e-bdae-b513e260c9c5', 'e0acd19b-5905-473e-828c-ef949891644c', 'aadf8efb-83cb-4f9b-be6f-c0e4feacb29b'],
            ['296deea0-b31b-482b-ae53-34bbe1046856', '4f564a36-6a45-41e2-b88c-aa503a83ea67', '6d0cdf9c-289f-4e5f-bff6-fb5e9a89c199'],
            ['6e7e595b-458e-46c0-88b8-92914f1eddfd', '18bce5fa-df83-4674-a17a-63dbf29424e1', '7a827bba-f783-43d2-b1a8-49e3ff0dfc5d'],
            ['3e72360b-24fb-40e3-be7e-abda6bec3881', '992a2efa-5778-4061-b4b8-f67c17bdd65b', '226fac94-c894-4d11-97a3-c494afd8e547'],
            ['61db6311-479f-489e-b62d-1b4152e6b218', '61510314-000b-436e-a65d-bb428e9135e0', 'a3853972-5c2e-48f1-a9a3-c2160a5b6d45']
        ]

        manchester_chart_data = [
            '311ac298-7349-43ed-b3b4-873b854e530c', '08a0a925-6b84-442c-bc4d-9c5054723072', 'e6a85832-5a96-44d8-b5a3-2416026669c4',
            '4d4d6829-3d94-4f18-afdb-527ecc8cc32e', '691ac1c5-3ba4-4809-b3e1-c16ed67724c8', '02b1dd75-1173-491e-96fa-0348d324ed46',
        ]

        if client_name == 'Wagner':
            return (eca_data_cumulative, eca_chart_data)

        elif client_name == 'Test One':
            return (desert_orth_data_cumulative, desert_orth_chart_data)

        elif client_name == 'Test Two':
            return (manchester_data, manchester_chart_data)


    def desert_ortho(id):
        pass

    
    