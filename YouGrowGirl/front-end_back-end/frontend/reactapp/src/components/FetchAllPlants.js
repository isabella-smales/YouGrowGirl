import { useState, useEffect } from "react";
import PlantTable from "./PlantTable";
import axios from "axios";

export default function FetchAllPlants() {
	// get data from API

	const [plants, getPlants] = useState("");

	// Unique token generated from https://docs.trefle.io/docs/guides/getting-started for plant JSON data

	const url =
		"https://trefle.io/api/v1/plants?token=KMu_Yl-TSeaxdSDjxpfMb51n4Z_ZUCNMs0rS2r0HBDE";

	useEffect(() => {
		getAllPlants();
	}, []);

	const getAllPlants = () => {
		axios
			.get(`${url}`,
			{ crossdomain: true }),
	})

			.then((response) => {
				const allPlants = response.data.plants.allPlants;

				// add plant data to state
				getPlants(allPlants);
			})
			.catch((error) => console.error(`Error: ${error}`));
	};

	return <PlantTable plants={plants} />;
}
