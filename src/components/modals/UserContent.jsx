import React from "react";

export default function UserContent({onClose, children}) {
    return (
        <div className="users">
            <button className="close" onClick={onClose}>Close</button>
            {children}
        </div>
    );
}
