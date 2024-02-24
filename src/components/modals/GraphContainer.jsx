import React from "react";
import "./styles/GraphContainer.css";

export default function GraphContainers({children}) {
    return (
        <div className="graph-container">
            {children}
        </div>
    );
}
