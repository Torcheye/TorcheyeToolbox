# Tasks: Vector Shape Generator

**Input**: Design documents from `/specs/001-shape-generator/`
**Prerequisites**: plan.md (✓), spec.md (✓), research.md (✓), data-model.md (✓), contracts/ (✓)

**Tests**: Tests are NOT requested in the feature specification. Manual testing only.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `- [ ] [ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single-file web app**: `shape-generator/index.html` (all HTML, CSS, JS embedded)
- **Documentation**: `shape-generator/README.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure (shape-generator/ with assets/ subdirectory)
- [X] T002 Create index.html file with HTML5 boilerplate in shape-generator/index.html
- [X] T003 [P] Add meta tags, title, and viewport configuration to shape-generator/index.html
- [X] T004 [P] Create README.md with user guide and feature description in shape-generator/README.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Add HTML structure (canvas element, controls panel container, modal overlay) to shape-generator/index.html
- [X] T006 Add embedded CSS with Grid layout (canvas | controls panel) and design system (typography, colors, spacing) to shape-generator/index.html
- [X] T007 Add shape type selector dropdown with Circle and Rectangle options to shape-generator/index.html
- [X] T008 Initialize JavaScript state object with AppState structure (currentShape, shapes, exportSettings, preferences) in shape-generator/index.html
- [X] T009 Implement Canvas initialization and browser feature detection in shape-generator/index.html
- [X] T010 Implement clearCanvas() function in shape-generator/index.html
- [X] T011 Implement hexToRGBA() color conversion utility function in shape-generator/index.html
- [X] T012 Implement validation functions (validateShapeProperty, validateExportSettings) in shape-generator/index.html
- [X] T013 Implement LocalStorage persistence functions (savePreferences, loadPreferences) in shape-generator/index.html
- [X] T014 Add application initialization logic (load preferences, check Canvas support, render initial shape) in shape-generator/index.html

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and Customize a Circle (Priority: P1) 🎯 MVP

**Goal**: Users can create and fully customize a circle shape with controls for radius, fill color, outline color, and outline thickness, with real-time preview

**Independent Test**: Open the app, select circle shape type, adjust radius slider (1-1000px), select fill color, select outline color, adjust outline thickness (0.5-50px), adjust opacity (0-100%), and verify the circle preview updates in real-time matching all selected properties

### Implementation for User Story 1

- [X] T015 [P] [US1] Add circle property controls HTML (radius slider + number input, fill color picker, stroke color picker, stroke width slider + number input, opacity slider + number input) to shape-generator/index.html
- [X] T016 [P] [US1] Add CSS styling for circle control inputs (sliders, color pickers, number inputs) to shape-generator/index.html
- [X] T017 [US1] Implement drawCircle() rendering function in shape-generator/index.html
- [X] T018 [US1] Implement event handler for circle radius slider and number input (sync values, update state, trigger render) in shape-generator/index.html
- [X] T019 [US1] Implement event handler for circle fill color picker (update state, trigger render) in shape-generator/index.html
- [X] T020 [US1] Implement event handler for circle stroke color picker (update state, trigger render) in shape-generator/index.html
- [X] T021 [US1] Implement event handler for circle stroke width slider and number input (sync values, validate 0.5-50px, update state, trigger render) in shape-generator/index.html
- [X] T022 [US1] Implement event handler for circle opacity slider and number input (sync values, validate 0-100%, update state, trigger render) in shape-generator/index.html
- [X] T023 [US1] Implement updateShape() function to handle property updates with validation in shape-generator/index.html
- [X] T024 [US1] Implement renderCurrentShape() function to clear canvas and draw current shape in shape-generator/index.html

**Checkpoint**: At this point, User Story 1 should be fully functional - users can create and customize circles with real-time preview

---

## Phase 4: User Story 2 - Create and Customize a Rectangle (Priority: P1)

**Goal**: Users can create and fully customize a rectangle shape with controls for width, height, fill color, outline color, and outline thickness, with real-time preview

**Independent Test**: Select rectangle shape type, adjust width and height sliders (1-1000px each), select fill and outline colors, adjust outline thickness (0.5-50px), adjust opacity (0-100%), and verify the rectangle preview updates in real-time matching all selected properties

### Implementation for User Story 2

- [X] T025 [P] [US2] Add rectangle property controls HTML (width slider + number input, height slider + number input, fill color picker, stroke color picker, stroke width slider + number input, opacity slider + number input) to shape-generator/index.html
- [X] T026 [P] [US2] Add CSS styling for rectangle control inputs (sliders, color pickers, number inputs) to shape-generator/index.html
- [X] T027 [US2] Implement drawRectangle() rendering function in shape-generator/index.html
- [X] T028 [US2] Implement event handler for rectangle width slider and number input (sync values, validate 1-1000px, update state, trigger render) in shape-generator/index.html
- [X] T029 [US2] Implement event handler for rectangle height slider and number input (sync values, validate 1-1000px, update state, trigger render) in shape-generator/index.html
- [X] T030 [US2] Implement event handlers for rectangle fill color, stroke color, stroke width, and opacity (reuse circle logic) in shape-generator/index.html

**Checkpoint**: At this point, User Stories 1 AND 2 should both work - users can create both circles and rectangles

---

## Phase 5: User Story 4 - Switch Between Shape Types (Priority: P2)

**Goal**: Users can switch between circle and rectangle shape types, with the UI showing appropriate controls for each shape and the canvas updating to display the selected shape

**Independent Test**: Create a circle with custom properties, switch to rectangle (verify UI shows rectangle controls and default rectangle appears), customize rectangle, switch back to circle (verify UI shows circle controls and default circle appears, previous customizations don't carry over inappropriately)

### Implementation for User Story 4

- [X] T031 [US4] Implement switchShape() function to handle shape type changes (update currentShape, show/hide control panels, render new shape) in shape-generator/index.html
- [X] T032 [US4] Implement event handler for shape type selector dropdown (call switchShape on change) in shape-generator/index.html
- [X] T033 [US4] Add CSS to toggle visibility of circle-controls and rectangle-controls sections based on selected shape type in shape-generator/index.html
- [X] T034 [US4] Update initialization logic to show correct controls panel on page load based on currentShape in shape-generator/index.html

**Checkpoint**: All shape creation user stories should now be independently functional - users can switch between shapes seamlessly

---

## Phase 6: User Story 3 - Export Shape as PNG (Priority: P2)

**Goal**: Users can export their customized shape as a PNG file with specified output dimensions and resolution (DPI), with validation for invalid inputs

**Independent Test**: Create any shape (circle or rectangle), click "Export to PNG" button, specify output width (e.g., 1920px), height (e.g., 1080px), and resolution (e.g., 300 DPI), confirm export, verify PNG file downloads with correct filename and specified dimensions, open the PNG file and verify it matches the canvas preview exactly. Also test validation by entering invalid dimensions (0, negative, >5000) and verify error messages appear.

### Implementation for User Story 3

- [X] T035 [P] [US3] Add export button HTML ("Export to PNG") to shape-generator/index.html
- [X] T036 [P] [US3] Add export modal dialog HTML (width input, height input, DPI input with presets, filename input, confirm/cancel buttons) to shape-generator/index.html
- [X] T037 [P] [US3] Add CSS styling for export button and modal dialog (overlay, centered dialog, form controls) to shape-generator/index.html
- [X] T038 [US3] Implement openExportModal() function to display export dialog with current export settings in shape-generator/index.html
- [X] T039 [US3] Implement closeExportModal() function to hide export dialog in shape-generator/index.html
- [X] T040 [US3] Implement event handlers for export modal inputs (width, height, DPI, filename) to update exportSettings state in shape-generator/index.html
- [X] T041 [US3] Implement exportToPNG() function (create temporary canvas, calculate DPI scale, render shape at export dimensions, generate PNG blob) in shape-generator/index.html
- [X] T042 [US3] Implement downloadBlob() function to trigger browser download with specified filename in shape-generator/index.html
- [X] T043 [US3] Implement export validation (check dimensions 1-5000px, validate DPI 1-600, validate filename format) in shape-generator/index.html
- [X] T044 [US3] Add error message display for invalid export parameters (inline error messages, red border on invalid fields) in shape-generator/index.html
- [X] T045 [US3] Implement event handler for export button click (open export modal) in shape-generator/index.html
- [X] T046 [US3] Implement event handler for export confirm button (validate, export, download, close modal) in shape-generator/index.html
- [X] T047 [US3] Implement event handler for export cancel button (close modal without exporting) in shape-generator/index.html

**Checkpoint**: All user stories should now be complete - users can create shapes, switch between types, and export as PNG

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and overall quality

- [X] T048 [P] Add performance optimization with requestAnimationFrame for render scheduling in shape-generator/index.html
- [X] T049 [P] Add debouncing for rapid slider updates (16ms delay) in shape-generator/index.html
- [ ] T050 [P] Add loading states and visual feedback during PNG export in shape-generator/index.html
- [X] T051 [P] Add accessibility improvements (ARIA labels, keyboard navigation, focus states) in shape-generator/index.html
- [X] T052 [P] Add error boundary for Canvas rendering failures with user-friendly error messages in shape-generator/index.html
- [X] T053 Code cleanup and refactoring (extract duplicate code, improve naming, add comments)
- [ ] T054 Validate against quickstart.md manual testing checklist
- [X] T055 [P] Update README.md with usage instructions, browser compatibility, and troubleshooting guide in shape-generator/README.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User Story 1 (Circle) can start after Foundational
  - User Story 2 (Rectangle) can start after Foundational (independent of US1)
  - User Story 4 (Switch) MUST complete after US1 and US2 (depends on both shapes being implemented)
  - User Story 3 (Export) can start after Foundational but benefits from having shapes to export
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (Circle - P1)**: Depends on Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (Rectangle - P1)**: Depends on Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (Switch - P2)**: Depends on US1 and US2 being complete (needs both shapes implemented)
- **User Story 3 (Export - P2)**: Depends on Foundational (Phase 2) - Can work independently but needs at least one shape to test

### Within Each User Story

- HTML controls before event handlers
- Render functions before event handlers that trigger rendering
- Validation functions before functions that use validation
- State update functions before event handlers

### Parallel Opportunities

- **Phase 1 (Setup)**: T001, T002, T003, T004 can all run in parallel
- **Phase 2 (Foundational)**: T006, T007 can run in parallel after T005
- **Phase 3 (US1)**: T015, T016 can run in parallel
- **Phase 4 (US2)**: T025, T026 can run in parallel
- **Phase 6 (US3)**: T035, T036, T037 can run in parallel
- **Phase 7 (Polish)**: T048, T049, T050, T051, T052, T055 can all run in parallel
- **User Stories**: US1 and US2 can be worked on in parallel by different developers after Foundational phase

---

## Parallel Example: User Story 1

```bash
# Launch HTML and CSS tasks for User Story 1 together:
Task: "Add circle property controls HTML to shape-generator/index.html"
Task: "Add CSS styling for circle control inputs to shape-generator/index.html"
```

## Parallel Example: Polish Phase

```bash
# Launch all polish tasks together:
Task: "Add performance optimization with requestAnimationFrame in shape-generator/index.html"
Task: "Add debouncing for rapid slider updates in shape-generator/index.html"
Task: "Add loading states during PNG export in shape-generator/index.html"
Task: "Add accessibility improvements in shape-generator/index.html"
Task: "Add error boundary for Canvas failures in shape-generator/index.html"
Task: "Update README.md with usage instructions in shape-generator/README.md"
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup (4 tasks)
2. Complete Phase 2: Foundational (10 tasks) - CRITICAL - blocks all stories
3. Complete Phase 3: User Story 1 - Circle (10 tasks)
4. Complete Phase 4: User Story 2 - Rectangle (6 tasks)
5. Complete Phase 5: User Story 4 - Switch Between Shapes (4 tasks)
6. **STOP and VALIDATE**: Test shape creation and switching independently
7. Ready for first demo/deployment

### Full Feature Delivery

1. Complete MVP (above)
2. Complete Phase 6: User Story 3 - Export (13 tasks)
3. **VALIDATE**: Test full export workflow with both shapes
4. Complete Phase 7: Polish (8 tasks)
5. **FINAL VALIDATION**: Run full quickstart.md testing checklist
6. Ready for production deployment

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (Circle) → Test independently → Demo
3. Add User Story 2 (Rectangle) → Test independently → Demo
4. Add User Story 4 (Switch) → Test independently → Demo (Basic MVP!)
5. Add User Story 3 (Export) → Test independently → Demo (Full Feature!)
6. Add Polish → Final validation → Production Ready!

---

## Task Summary

**Total Tasks**: 55

**By Phase**:
- Phase 1 (Setup): 4 tasks
- Phase 2 (Foundational): 10 tasks
- Phase 3 (User Story 1 - Circle): 10 tasks
- Phase 4 (User Story 2 - Rectangle): 6 tasks
- Phase 5 (User Story 4 - Switch): 4 tasks
- Phase 6 (User Story 3 - Export): 13 tasks
- Phase 7 (Polish): 8 tasks

**By User Story**:
- User Story 1 (Circle - P1): 10 tasks
- User Story 2 (Rectangle - P1): 6 tasks
- User Story 4 (Switch - P2): 4 tasks
- User Story 3 (Export - P2): 13 tasks

**Parallel Opportunities**: 15 tasks marked [P] for parallel execution

**Independent Test Criteria**:
- User Story 1: Can create and customize circles with real-time preview
- User Story 2: Can create and customize rectangles with real-time preview
- User Story 4: Can switch between shape types seamlessly
- User Story 3: Can export shapes as PNG with custom dimensions and DPI

**Suggested MVP Scope**: User Stories 1, 2, and 4 (shape creation and switching) = 20 implementation tasks + 14 foundational tasks = 34 tasks total

---

## Notes

- [P] tasks = different sections/concerns, can be worked on in parallel
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Single-file architecture means all tasks modify the same file (index.html)
- Commit after each logical group of tasks (e.g., after each phase)
- Stop at any checkpoint to validate story independently
- Manual testing only (no automated tests requested in spec)
- Estimated implementation time: 8-10 hours for MVP (per quickstart.md)
