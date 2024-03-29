import React, { useState } from "react";
import UserContent from "./modals/UserContent";
import AdminData from "./AdminData";
import DemoData from "./DemoData";
import "./styles/Content.css";

export default function Content() {
    // States for Content Buttons
    const [isAdmin, setAdmin] = useState(false);
    const [isDemo, setDemo] = useState(false);

    function openAdmin() {
        setAdmin(true);
        setDemo(false);
    }

    function openDemo() {
        setDemo(true);
        setAdmin(false);
    }

    function closeAdmin() {
        setAdmin(false);
    }

    function closeDemo() {
        setDemo(false);
    }

    return (
        <div className="content">
            <div className="user-options">
                <button 
                    id="user-btns" 
                    onClick={openAdmin} 
                    className={isAdmin ? "active" : ""}
                >
                    Admin User
                </button> 
                <button 
                    id="user-btns" 
                    onClick={openDemo} 
                    className={isDemo ? "active" : ""}
                >
                    Demo User
                </button>
            </div>
            <div className="user-graphs">
                {isAdmin && (
                    <UserContent onClose={closeAdmin}>
                        <AdminData />
                    </UserContent>
                )}
                
                {isDemo && (
                    <UserContent onClose={closeDemo}>
                        <DemoData />
                    </UserContent>
                )}
            </div>
        </div>
    );
}
