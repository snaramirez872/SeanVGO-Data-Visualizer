import React from "react";
import "./styles/Header.css";

export default function Header() {
    return (
        <div className="Header">
            <h1 className="logo">
                <p>SeanVGO Data Visualizer</p>
            </h1>
            <a href="https://seanvgo-f931c.web.app/login" target="_blank" rel="noreferrer">
                <p className="vgo-btn">SeanVGO</p>
            </a>
        </div>
    );
}
