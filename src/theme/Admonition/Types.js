import React from "react";
import DefaultAdmonitionTypes from "@theme-original/Admonition/Types";

function CodeBox(props) {
    return (
        <div style={{ border: "solid red", padding: 10 }}>
            <h5 style={{ color: "blue", fontSize: 30 }}>{props.title}</h5>
            <div>{props.children}</div>
        </div>
    );
}

function ExampleBox(props) {
    return (
        <div style={{ border: "solid red", padding: 10 }}>
            <h5 style={{ color: "blue", fontSize: 30 }}>{props.title}</h5>
            <div>{props.children}</div>
        </div>
    );
}

function CenterBox(props) {
    return (
        <div style={{ border: "solid red", padding: 10 }}>
            <h5 style={{ color: "blue", fontSize: 30 }}>{props.title}</h5>
            <div>{props.children}</div>
        </div>
    );
}
const AdmonitionTypes = {
    ...DefaultAdmonitionTypes,

    // Add all your custom admonition types here...
    // You can also override the default ones if you want
    codebox: CodeBox,
    example: ExampleBox,
    center: CenterBox,
};

export default AdmonitionTypes;
