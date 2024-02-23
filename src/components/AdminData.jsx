import React from "react";
import GraphContainers from "./modals/GraphContainer";
import AdminGenres from "../assets/graphs/admin-user/genre-graph.png"
import AdminPlats from "../assets/graphs/admin-user/plats-graph.png"

export default function AdminData() {
    return (
        <div className="admin-data">
            <GraphContainers>
                <h2>Genres</h2>
                <img src={AdminGenres} alt="" />
            </GraphContainers>
            <GraphContainers>
                <h2>Platforms</h2>
                <img src={AdminPlats} alt="" />
            </GraphContainers>
        </div>
    );
}
