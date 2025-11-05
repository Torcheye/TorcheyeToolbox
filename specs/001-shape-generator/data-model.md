# Data Model: Vector Shape Generator

**Phase**: 1 - Design & Contracts
**Date**: 2025-11-04
**Status**: Complete

## Overview

This document defines the data structures and state management for the Vector Shape Generator application. Since this is a client-side only application with no backend, the "data model" represents JavaScript object structures and their validation rules.

## Core Entities

### 1. AppState

The root state object containing all application data.

```typescript
interface AppState {
  currentShape: ShapeType;
  shapes: {
    circle: CircleShape;
    rectangle: RectangleShape;
  };
  exportSettings: ExportSettings;
  preferences: UserPreferences;
}
```

**Fields**:
- `currentShape`: Currently selected shape type ('circle' | 'rectangle')
- `shapes`: Configuration for each shape type
- `exportSettings`: PNG export parameters
- `preferences`: User preferences (persisted to localStorage)

**Validation Rules**:
- `currentShape` must be one of the defined shape types
- `shapes` object must contain entries for all supported shape types

**State Transitions**:
- User selects shape type → Update `currentShape`
- User adjusts shape properties → Update corresponding shape object
- User modifies export settings → Update `exportSettings`

---

### 2. CircleShape

Represents a circle with customizable properties.

```typescript
interface CircleShape {
  radius: number;
  fillColor: string;
  strokeColor: string;
  strokeWidth: number;
  opacity: number;
}
```

**Fields**:
- `radius`: Circle radius in pixels
- `fillColor`: Interior fill color (hex format: #RRGGBB)
- `strokeColor`: Outline stroke color (hex format: #RRGGBB)
- `strokeWidth`: Outline thickness in pixels
- `opacity`: Transparency level (0-100%)

**Validation Rules**:
- `radius`: 1 ≤ radius ≤ 1000 (positive integer)
- `fillColor`: Valid hex color (#000000 to #FFFFFF)
- `strokeColor`: Valid hex color (#000000 to #FFFFFF)
- `strokeWidth`: 0.5 ≤ strokeWidth ≤ 50 (allows decimal values)
- `opacity`: 0 ≤ opacity ≤ 100 (integer percentage)

**Default Values**:
```javascript
{
  radius: 100,
  fillColor: '#ffffff',
  strokeColor: '#000000',
  strokeWidth: 2,
  opacity: 100
}
```

**Relationships**:
- Selected when `AppState.currentShape === 'circle'`
- Used as input for `CanvasRenderer.drawCircle()`

---

### 3. RectangleShape

Represents a rectangle with customizable properties.

```typescript
interface RectangleShape {
  width: number;
  height: number;
  fillColor: string;
  strokeColor: string;
  strokeWidth: number;
  opacity: number;
}
```

**Fields**:
- `width`: Rectangle width in pixels
- `height`: Rectangle height in pixels
- `fillColor`: Interior fill color (hex format: #RRGGBB)
- `strokeColor`: Outline stroke color (hex format: #RRGGBB)
- `strokeWidth`: Outline thickness in pixels
- `opacity`: Transparency level (0-100%)

**Validation Rules**:
- `width`: 1 ≤ width ≤ 1000 (positive integer)
- `height`: 1 ≤ height ≤ 1000 (positive integer)
- `fillColor`: Valid hex color (#000000 to #FFFFFF)
- `strokeColor`: Valid hex color (#000000 to #FFFFFF)
- `strokeWidth`: 0.5 ≤ strokeWidth ≤ 50 (allows decimal values)
- `opacity`: 0 ≤ opacity ≤ 100 (integer percentage)

**Default Values**:
```javascript
{
  width: 200,
  height: 150,
  fillColor: '#ffffff',
  strokeColor: '#000000',
  strokeWidth: 2,
  opacity: 100
}
```

**Relationships**:
- Selected when `AppState.currentShape === 'rectangle'`
- Used as input for `CanvasRenderer.drawRectangle()`

---

### 4. ExportSettings

Configuration for PNG export functionality.

```typescript
interface ExportSettings {
  width: number;
  height: number;
  dpi: number;
  filename: string;
}
```

**Fields**:
- `width`: Output image width in pixels
- `height`: Output image height in pixels
- `dpi`: Dots per inch (resolution)
- `filename`: Export filename (without .png extension)

**Validation Rules**:
- `width`: 1 ≤ width ≤ 5000 (positive integer)
- `height`: 1 ≤ height ≤ 5000 (positive integer)
- `dpi`: Must be one of [72, 150, 300] or custom value 1-600
- `filename`: Non-empty string, alphanumeric + hyphens/underscores

**Default Values**:
```javascript
{
  width: 800,
  height: 600,
  dpi: 72,
  filename: 'shape-export'
}
```

**Relationships**:
- Used by `ExportManager.exportToPNG()` to generate PNG blob
- Displayed in export dialog UI

---

### 5. UserPreferences

User preferences persisted across sessions.

```typescript
interface UserPreferences {
  rememberLastShape: boolean;
  lastShapeType: ShapeType | null;
  lastExportSettings: Partial<ExportSettings>;
}
```

**Fields**:
- `rememberLastShape`: Whether to restore previous session state
- `lastShapeType`: Last selected shape type
- `lastExportSettings`: Last used export configuration

**Validation Rules**:
- `rememberLastShape`: Boolean
- `lastShapeType`: 'circle' | 'rectangle' | null
- `lastExportSettings`: Partial match to ExportSettings schema

**Default Values**:
```javascript
{
  rememberLastShape: true,
  lastShapeType: null,
  lastExportSettings: {}
}
```

**Persistence**:
- Stored in `localStorage.getItem('shapeGeneratorPreferences')`
- Loaded on application initialization
- Updated on user actions (shape selection, export)

---

## Type Definitions

### ShapeType

```typescript
type ShapeType = 'circle' | 'rectangle';
```

Enumeration of supported shape types.

---

### Color

```typescript
type Color = string; // Hex format: #RRGGBB
```

Represents RGB colors in hexadecimal format.

**Validation Pattern**: `/^#[0-9A-Fa-f]{6}$/`

**Conversion Utilities**:
```javascript
// Hex to RGBA (with opacity)
function hexToRGBA(hex: string, opacity: number): string {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  const a = opacity / 100;
  return `rgba(${r}, ${g}, ${b}, ${a})`;
}

// Validate hex color
function isValidHex(color: string): boolean {
  return /^#[0-9A-Fa-f]{6}$/.test(color);
}
```

---

## State Management

### State Update Flow

```
User Interaction (UI Event)
    ↓
Event Handler (updateShape(), updateExport())
    ↓
Validation (validateShapeData(), validateExportSettings())
    ↓
State Mutation (state.shapes[type].property = value)
    ↓
Side Effects:
  - Canvas Redraw (renderCurrentShape())
  - UI Sync (updateInputValues())
  - Persistence (savePreferences())
```

### State Update Functions

```javascript
// Update current shape properties
function updateShape(property, value) {
  const shapeType = state.currentShape;
  const shape = state.shapes[shapeType];

  // Validate
  if (!validateProperty(shapeType, property, value)) {
    showValidationError(property, value);
    return false;
  }

  // Update state
  shape[property] = value;

  // Trigger side effects
  renderCurrentShape();
  savePreferences();

  return true;
}

// Switch shape type
function switchShape(newType) {
  if (!['circle', 'rectangle'].includes(newType)) {
    throw new Error(`Invalid shape type: ${newType}`);
  }

  state.currentShape = newType;

  // Reset to defaults for new shape
  resetShapeToDefaults(newType);

  // Render new shape
  renderCurrentShape();

  // Update UI
  updateControlPanel(newType);
}

// Update export settings
function updateExportSettings(property, value) {
  // Validate
  if (!validateExportProperty(property, value)) {
    showValidationError(property, value);
    return false;
  }

  // Update state
  state.exportSettings[property] = value;

  // Update preview (if dimension changed)
  if (['width', 'height', 'dpi'].includes(property)) {
    updateExportPreview();
  }

  return true;
}
```

---

## Validation Schema

### CircleShape Validation

```javascript
const circleValidation = {
  radius: {
    min: 1,
    max: 1000,
    type: 'integer',
    message: 'Radius must be between 1 and 1000 pixels'
  },
  fillColor: {
    pattern: /^#[0-9A-Fa-f]{6}$/,
    message: 'Fill color must be a valid hex color (#RRGGBB)'
  },
  strokeColor: {
    pattern: /^#[0-9A-Fa-f]{6}$/,
    message: 'Stroke color must be a valid hex color (#RRGGBB)'
  },
  strokeWidth: {
    min: 0.5,
    max: 50,
    type: 'number',
    message: 'Stroke width must be between 0.5 and 50 pixels'
  },
  opacity: {
    min: 0,
    max: 100,
    type: 'integer',
    message: 'Opacity must be between 0 and 100%'
  }
};
```

### RectangleShape Validation

```javascript
const rectangleValidation = {
  width: {
    min: 1,
    max: 1000,
    type: 'integer',
    message: 'Width must be between 1 and 1000 pixels'
  },
  height: {
    min: 1,
    max: 1000,
    type: 'integer',
    message: 'Height must be between 1 and 1000 pixels'
  },
  fillColor: {
    pattern: /^#[0-9A-Fa-f]{6}$/,
    message: 'Fill color must be a valid hex color (#RRGGBB)'
  },
  strokeColor: {
    pattern: /^#[0-9A-Fa-f]{6}$/,
    message: 'Stroke color must be a valid hex color (#RRGGBB)'
  },
  strokeWidth: {
    min: 0.5,
    max: 50,
    type: 'number',
    message: 'Stroke width must be between 0.5 and 50 pixels'
  },
  opacity: {
    min: 0,
    max: 100,
    type: 'integer',
    message: 'Opacity must be between 0 and 100%'
  }
};
```

### ExportSettings Validation

```javascript
const exportValidation = {
  width: {
    min: 1,
    max: 5000,
    type: 'integer',
    message: 'Export width must be between 1 and 5000 pixels'
  },
  height: {
    min: 1,
    max: 5000,
    type: 'integer',
    message: 'Export height must be between 1 and 5000 pixels'
  },
  dpi: {
    min: 1,
    max: 600,
    type: 'integer',
    suggested: [72, 150, 300],
    message: 'DPI must be between 1 and 600 (common: 72, 150, 300)'
  },
  filename: {
    pattern: /^[a-zA-Z0-9_-]+$/,
    maxLength: 50,
    message: 'Filename must be alphanumeric with hyphens/underscores (max 50 chars)'
  }
};
```

---

## Data Flow Diagram

```
┌─────────────────┐
│   User Input    │
│  (UI Controls)  │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Event Handler  │
│   (UI Layer)    │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   Validation    │
│    (Logic)      │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   State Mutation│
│   (AppState)    │
└────────┬────────┘
         │
         v
    ┌────┴────┐
    │         │
    v         v
┌───────┐ ┌─────────────┐
│Canvas │ │  LocalStorage│
│Render │ │ Persistence  │
└───────┘ └─────────────┘
```

---

## Initialization

### Application Bootstrap

```javascript
// 1. Load preferences from localStorage
const savedPrefs = loadPreferences();

// 2. Initialize state with defaults
const state = {
  currentShape: savedPrefs.rememberLastShape
    ? (savedPrefs.lastShapeType || 'circle')
    : 'circle',
  shapes: {
    circle: { ...defaultCircle },
    rectangle: { ...defaultRectangle }
  },
  exportSettings: {
    ...defaultExportSettings,
    ...savedPrefs.lastExportSettings
  },
  preferences: savedPrefs
};

// 3. Check Canvas support
if (!checkCanvasSupport()) {
  showUnsupportedBrowserError();
  return;
}

// 4. Initialize UI
initializeControlPanel(state.currentShape);
syncUIWithState();

// 5. Render initial shape
renderCurrentShape();
```

---

## Persistence Strategy

### LocalStorage Schema

```javascript
// Key: 'shapeGeneratorPreferences'
{
  "rememberLastShape": true,
  "lastShapeType": "circle",
  "lastExportSettings": {
    "width": 1920,
    "height": 1080,
    "dpi": 300,
    "filename": "my-circle"
  },
  "version": "1.0.0" // Schema version for future migrations
}
```

### Save Operations

- **Trigger**: On every state change (debounced to avoid excessive writes)
- **Method**: `localStorage.setItem('shapeGeneratorPreferences', JSON.stringify(prefs))`
- **Error Handling**: Catch QuotaExceededError, fallback to session-only state

### Load Operations

- **Trigger**: On application initialization
- **Method**: `JSON.parse(localStorage.getItem('shapeGeneratorPreferences'))`
- **Error Handling**: Catch SyntaxError (corrupted data), fallback to defaults

---

## Summary

The data model is intentionally simple, using plain JavaScript objects with explicit validation rules. There are no complex relationships or database constraints—just client-side state management with localStorage persistence. This aligns with the constitution's Simplicity First principle while supporting all feature requirements.

**Key Design Decisions**:
1. **Flat State Structure**: Easy to serialize and deserialize
2. **Explicit Validation**: Clear rules for each property
3. **Default Values**: Sensible fallbacks for all fields
4. **Type Safety**: TypeScript interfaces document contracts (optional runtime use)
5. **Persistence**: LocalStorage for UX improvement, not critical functionality

**Ready to proceed**: Data model is complete and validated against feature requirements.
