describe('template spec', () => {

it('default', () => {
    cy.visit("http://localhost:9000/qrcode/")
    cy.get('#result_qr_code').should('not.have.attr', 'src')
    cy.get('button.btn').click()
    cy.get('#result_qr_code').should('have.attr', 'src')
});

it("test error", () => {
    cy.visit("http://localhost:9000/qrcode/")
    cy.get('#result_qr_code').should('not.have.attr', 'src')
    cy.get('.invalid-feedback').should("not.be.visible")
    cy.get('#url').focus().clear()
    cy.get('button.btn').click()
    cy.get('#result_qr_code').should('not.have.attr', 'src')
    cy.get('.invalid-feedback').should("contain", "URL is required")
    cy.get('.invalid-feedback').should("be.visible")
});


it("test sliders", () => {
    cy.visit("http://localhost:9000/qrcode/")
    cy.get('#box_size').click({ multiple: true, force: true })
    cy.get('#box_size').type("{rightarrow}{rightarrow}")
    cy.get('#box_size').type("{rightarrow}{rightarrow}")
    cy.get('#box_size').type("{rightarrow}{rightarrow}")
    cy.get('#box_size').type("{rightarrow}{rightarrow}")
    cy.get('#box_size').type("{rightarrow}{rightarrow}")
    cy.get('#box_size').type("{rightarrow}{rightarrow}")

});

})
