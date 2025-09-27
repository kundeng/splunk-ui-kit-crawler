---
title: '@splunk/react-ui - 5.3.0'
url: https://splunkui.splunk.com/Packages/react-ui/CardLayout
type: component
crawled_at: '2025-09-27T01:49:56.718013'
package: react-ui
component: CardLayout
tags:
- react-ui
- component
---

## Examples

Card Layout provides a container to responsively arrange and resize Cards.


### Example 1

```jsx
import React, { Component } from 'react';

import styled from 'styled-components';

import Card from '@splunk/react-ui/Card';
import CardLayout from '@splunk/react-ui/CardLayout';
import ControlGroup from '@splunk/react-ui/ControlGroup';
import Number from '@splunk/react-ui/Number';
import Select from '@splunk/react-ui/Select';
import Switch from '@splunk/react-ui/Switch';
import { variables } from '@splunk/themes';

const StyledWrapper = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    column-gap: ${variables.spacingXLarge};

    /* 5th child is the first checkbox, which we want to start on a new row */
    & > :nth-child(5) {
        grid-column: 1;
    }
`;

const StyledCardContent = styled.div`
    height: 200px;
    background: ${variables.neutral200};
`;

class Interactive extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: 5,
            minWidth: 200,
            maxWidth: 600,
            gutterSize: 10,
            wrapCards: true,
            alignCards: 'left',
            setAsWidth: false,
            hasMaxWidth: false,
        };
    }

    handleChangeAmount = (e, { value }) => {
        this.setState({ value });
    };

    handleChangeMinWidth = (e, { value }) => {
        this.setState({ minWidth: value });
        if (this.state.setAsWidth) {
            this.setState({ maxWidth: value });
        }
    };

    handleChangeMaxWidth = (e, { value }) => {
        this.setState({ maxWidth: value });
    };

    handleChangeGutter = (e, { value }) => {
        this.setState({ gutterSize: value });
    };

    handleChangeWrap = (e, { value }) => {
        this.setState({ wrapCards: !value });
    };


    handleChangeAlign = (e, { value }) => {
        this.setState({ alignCards: value });
    };

    handleSetAsWidth = (e, { value }) => {
        this.setState({ setAsWidth: !value });
    };

    handleHasMaxWidth = (e, { value }) => {
        this.setState({ hasMaxWidth: !value });
    };

    render() {
        const cards = [];
        for (let i = 0; i < (this.state.value ?? 0); i += 1) {
            cards.push(
                <Card key={i}>
                    <Card.Header title={`Card ${i + 1}`} />
                    <Card.Body>
                        <StyledCardContent />
                    </Card.Body>
                </Card>
            );
        }
        return (
            <article>
                <StyledWrapper>
                    <ControlGroup label="Number of cards">
                        <Number
                            value={this.state.value}
                            onChange={this.handleChangeAmount}
                            min={1}
                            max={100}
                        />
                    </ControlGroup>
                    <ControlGroup label="Gutter size">
                        <Number
                            value={this.state.gutterSize}
                            onChange={this.handleChangeGutter}
                            min={0}
                            max={50}
                            step={5}
                        />
                    </ControlGroup>
                    <ControlGroup label="Align cards">
                        <Select value={this.state.alignCards} onChange={this.handleChangeAlign}>
                            <Select.Option label="Left" value="left" />
                            <Select.Option label="Center" value="center" />
                            <Select.Option label="Right" value="right" />
                        </Select>
                    </ControlGroup>
                    <ControlGroup
                        label={
                            this.state.setAsWidth ||
                            (!this.state.setAsWidth && this.state.hasMaxWidth)
                                ? 'Card width'
                                : 'Card min width'
                        }
                        style={{
                            marginBottom:
                                this.state.hasMaxWidth && !this.state.setAsWidth ? 2 : undefined,
                        }}
                    >
                        <Number
                            value={this.state.minWidth}
                            onChange={this.handleChangeMinWidth}
                            min={100}
                            max={1000}
                            step={50}
                        />

                        {this.state.hasMaxWidth && !this.state.setAsWidth && (
                            <Number
                                value={this.state.maxWidth}
                                onChange={this.handleChangeMaxWidth}
                                min={100}
                                max={2000}
                                step={50}
                            />
                        )}
                        {!this.state.setAsWidth && this.state.hasMaxWidth && (
                            <ControlGroup label=" ">
                                <div style={{ width: '50%' }}>Min</div>
                                <div style={{ width: '50%', marginLeft: 10 }}>Max</div>
                            </ControlGroup>
                        )}
                    </ControlGroup>
                    <ControlGroup label="Wrap cards">
                        <Switch
                            value={this.state.wrapCards}
                            onClick={this.handleChangeWrap}
                            selected={this.state.wrapCards}
                            appearance="toggle"
                        />
                    </ControlGroup>
                    <ControlGroup label="Width only">
                        <Switch
                            value={this.state.setAsWidth}
                            onClick={this.handleSetAsWidth}
                            selected={this.state.setAsWidth}
                            appearance="toggle"
                        />
                    </ControlGroup>
                    <ControlGroup label="Show max width">
                        <Switch
                            value={this.state.hasMaxWidth}
                            onClick={this.handleHasMaxWidth}
                            selected={this.state.hasMaxWidth}
                            appearance="toggle"
                            disabled={this.state.setAsWidth}
                        />
                    </ControlGroup>
                </StyledWrapper>
                <CardLayout
                    alignCards={this.state.alignCards}
                    gutterSize={this.state.gutterSize}
                    cardWidth={this.state.setAsWidth ? this.state.minWidth : undefined}
                    cardMinWidth={this.state.minWidth || undefined}
                    cardMaxWidth={this.state.hasMaxWidth ? this.state.maxWidth : undefined}
                    wrapCards={this.state.wrapCards}
                >
                    {cards}
                </CardLayout>
            </article>
        );
    }
}

export default Interactive;
```

### Example 2

```jsx
import React from 'react';

import styled from 'styled-components';

import Card from '@splunk/react-ui/Card';
import CardLayout from '@splunk/react-ui/CardLayout';
import { variables } from '@splunk/themes';

const StyledCardContent = styled.div`
    height: 200px;
    background: ${variables.neutral200};
`;

function Basic() {
    const cardContent = <StyledCardContent />;

    return (
        <CardLayout style={{ maxWidth: 900 }}>
            <Card>
                <Card.Header title="Card 1" />
                <Card.Body>{cardContent}</Card.Body>
            </Card>
            <Card>
                <Card.Header title="Card 2" />
                <Card.Body>{cardContent}</Card.Body>
            </Card>
            <Card>
                <Card.Header title="Card 3" />
                <Card.Body>{cardContent}</Card.Body>
            </Card>
        </CardLayout>
    );
}

export default Basic;
```
## API

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no
PropType:| oneOfType(number, string)
---|---
Required:| no
PropType:| oneOfType(number, string)
---|---
Required:| no
PropType:| oneOfType(number, string)
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| number
---|---
Default:| 10
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no

### CardLayout API

#### Props

alignCards

Aligns `Card`s in layout.

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no

cardMaxWidth

Sets maximum width of each `Card`.

PropType:| oneOfType(number, string)
---|---
Required:| no

cardMinWidth

Sets minimum width of each `Card`.

PropType:| oneOfType(number, string)
---|---
Required:| no

cardWidth

Sets width of each `Card`.

PropType:| oneOfType(number, string)
---|---
Required:| no

children

Must be `Card`.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

gutterSize

Sets space in pixels between each `Card`.

PropType:| number
---|---
Default:| 10
Required:| no

wrapCards

Lets `Card`s wrap to a new line when the container gets narrow.

PropType:| bool
---|---
Default:| true
Required:| no

#### Props

alignCards

Aligns `Card`s in layout.

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no

cardMaxWidth

Sets maximum width of each `Card`.

PropType:| oneOfType(number, string)
---|---
Required:| no

cardMinWidth

Sets minimum width of each `Card`.

PropType:| oneOfType(number, string)
---|---
Required:| no

cardWidth

Sets width of each `Card`.

PropType:| oneOfType(number, string)
---|---
Required:| no

children

Must be `Card`.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

gutterSize

Sets space in pixels between each `Card`.

PropType:| number
---|---
Default:| 10
Required:| no

wrapCards

Lets `Card`s wrap to a new line when the container gets narrow.

PropType:| bool
---|---
Default:| true
Required:| no

## Test Hooks

#### Element Selectors

card-layout

The root of the `CardLayout`.

Example:| [data-test="card-layout"]
---|---
Attribute:| data-test
Value:| cardlayout
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

