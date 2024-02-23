import React from "react";
import GraphContainers from "./modals/GraphContainer";
import DemoGenres from "../assets/graphs/test-user/genre-graph.png"
import DemoPlats from "../assets/graphs/test-user/plats-graph.png"

export default function DemoData() {
    return (
        <div className="demo-data">
            <GraphContainers>
                <h2>Genres</h2>
                <img src={DemoGenres} alt="" />
            </GraphContainers>
            <GraphContainers>
                <h2>Platforms</h2>
                <img src={DemoPlats} alt="" />
            </GraphContainers>
        </div>
    );
}
